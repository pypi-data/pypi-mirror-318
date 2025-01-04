import google.generativeai as genai
from argparse import ArgumentParser
from dotenv import load_dotenv
import sys
from termcolor import cprint
import time
import os
from datetime import datetime, timedelta
from get_code_from_markdown import get_code_from_markdown
import json
from json import JSONDecodeError

def list_all_files(directory):
    """
    Lists all files in the given directory and its subdirectories.
    Args:
        directory (str): The root directory path to start searching from
    Returns:
        list: A list of tuples containing (file_path, last_modified_time)
    """
    all_files = []
    try:
        # Walk through directory and subdirectories
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                # Get last modified time
                last_modified = datetime.fromtimestamp(os.path.getmtime(file_path))
                all_files.append((file_path, last_modified))
    except PermissionError as e:
        print(f"Permission denied accessing some paths: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    return all_files, [fl[0] for fl in all_files]

def list_recently_modified_files(directory, hours=1):
    """
    Lists files modified within the specified number of hours in the directory
    and its subdirectories.
    Args:
        directory (str): The root directory path to start searching from
        hours (int): Number of hours to look back (default is 1)
    Returns:
        list: A list of tuples containing (file_path, last_modified_time)
    """
    # Get current time
    current_time = datetime.now()
    # Calculate the cutoff time
    cutoff_time = current_time - timedelta(hours=hours)
    # Get all files
    all_files, alfls = list_all_files(directory)
    # Filter for recently modified files
    recent_files = [
        (file_path, mod_time)
        for file_path, mod_time in all_files
        if mod_time >= cutoff_time
    ]
    return recent_files, [fl[0] for fl in recent_files]

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

def wait_for_files_active(files):
    """Waits for the given files to be active.

    Some files uploaded to the Gemini API need to be processed before they can be
    used as prompt inputs. The status can be seen by querying the file's "state"
    field.

    This implementation uses a simple blocking polling loop. Production code
    should probably employ a more sophisticated approach.
    """
    for name in (file.name for file in files):
        file = genai.get_file(name)
        while file.state.name == "PROCESSING":
            time.sleep(10)
        file = genai.get_file(name)
        if file.state.name != "ACTIVE":
            raise Exception(f"File {file.name} failed to process")

def get_json(content: str) -> dict:
    try:
        data = json.loads(content)
        return data
    except JSONDecodeError:
        code = get_code_from_markdown(content, language="json")[0]
        data = json.loads(code)
        return data

def main():
    parser = ArgumentParser()
    parser.add_argument("-d", "--directory", help="Directory containing Obsidian notes for which to produce the digest", type=str, required=True)
    parser.add_argument("-a", "--allfiles", help="Produce the digest for all the files in the directory, and not only for those modified in the last hour", action="store_true", required=False, default=False)
    parser.add_argument("-k", "--apikey", help="Provide your Google Gemini API key either as a path to your .env file containing the GOOGLE_API_KEY variable, the name of the environmental variable under which the key is stored or the key itself (the first two methods are suggested)", required=True, type=str)
    parser.add_argument("-s", "--save", help="Save the digest as a Markdown File in your Obsidian vault", required=False, action="store_true", default=False)

    args = parser.parse_args()
    dirr = args.directory
    allf = args.allfiles
    apk = args.apikey
    sav = args.save

    if not os.path.exists(dirr):
        cprint("ERROR! The provided directory does not exist", color="red", attrs=["bold"], file=sys.stderr)
        sys.exit(1)
    else:
        if not load_dotenv(apk):
            if not os.getenv(apk):
                apikey = apk
                cprint(f"WARNING! Seems like you passed your API key directly from command line: this behavior is not advised, use a .env file or an environmental variable instead.", color="magenta", attrs=["bold"], file=sys.stderr)
            else:
                apikey = os.getenv(apk)
        else:
            apikey = os.getenv("GOOGLE_API_KEY")
            if not apikey:
                cprint("ERROR! The provided API key entry is neither a path to an .env file containing the GOOGLE_API_KEY variable, nor the name of an environment variable neither the API key itself. Please, provide one of those inputs.", color="red", attrs=["bold"], file=sys.stderr)
                sys.exit(2)
        try:
            genai.configure(api_key=apikey)
        except Exception as e:
            cprint(f"ERROR! The provided API key does not seem to be valid and returns the following error\n\n{e}\n", color="red", attrs=["bold"], file=sys.stderr)
            sys.exit(3)
        else:
            if allf:
                files = list_all_files(dirr)[1]
                files = [f for f in files if f.endswith(".md")]
                cprint(f"WARNING! You said that you should take into account all files: this behavior is not advised, as it could result in lots of API calls, consuming resources and money", color="magenta", attrs=["bold"], file=sys.stderr)
            else:
                files = list_recently_modified_files(dirr)[1]
                files = [f for f in files if f.endswith(".md")]
            generation_config = {
                    "temperature": 0,
                    "top_p": 0.95,
                    "top_k": 40,
                    "max_output_tokens": 8192,
                    "response_mime_type": "text/plain",
                }
            try:
                model = genai.GenerativeModel(
                    model_name="gemini-2.0-flash-exp",
                    generation_config=generation_config,
                )
            except Exception as e: 
                cprint(f"ERROR! There was an error while loading Gemini model:\n\n{e}\n", color="red", attrs=["bold"], file=sys.stderr)
                sys.exit(5)
            else:
                chat_session = model.start_chat(
                    history=[]
                )
                if len(files) > 0:
                    for fl in files:
                        try:
                            upfl = upload_to_gemini(fl, mime_type="text/plain")
                        except Exception as e:
                            cprint(f"WARNING! There was an error while uploading the file {fl} to Gemini:\n\n{e}\n", color="magenta", attrs=["bold"], file=sys.stderr)
                            continue
                        else:
                            try:
                                response = chat_session.send_message([upfl, """Generate, for the uploaded file, a digest, which you should output in JSON format following this example:
                                ```json
                                {
                                    "style_suggestions": "Suggestions about style, formulation, grammar and syntax",
                                    "content_suggestions": "Suggestions related to the content of the file",
                                    "general_considerations": "General consideration on the document",
                                
                                }
                                ```
                                Use also the previous information from this chat, if you think it is relevant. Output inly thr JSON string"""])
                            except Exception as e:
                                cprint(f"WARNING! There was an error in generating the response from Gemini:\n\n{e}", color="magenta", attrs=["bold"], file=sys.stderr)
                                continue
                            else:
                                try:
                                    d = get_json(response.text)
                                except Exception as e:
                                    cprint(f"WARNING! There was an error in parsing response from Gemini:\n\n{e}", color="magenta", attrs=["bold"], file=sys.stderr)
                                try:
                                    doc = ""
                                    cprint(f"Style suggestions for {fl}✍️", color="green", attrs=["bold"])
                                    print(d["style_suggestions"])
                                    doc += f"### Style suggestions✍️\n\n{d['style_suggestions']}\n\n"
                                    cprint(f"Content suggestions for {fl}💡", color="green", attrs=["bold"])
                                    print(d["content_suggestions"])
                                    doc += f"### Content suggestions💡\n\n{d['content_suggestions']}\n\n"
                                    cprint(f"General considerations for {fl}🧠", color="green", attrs=["bold"])
                                    print(d["general_considerations"])
                                    doc += f"### General considerations🧠\n\n{d['general_considerations']}\n\n"
                                except:
                                    cprint(f"WARNING! There was an error in parsing response from Gemini:\n\n{e}", color="magenta", attrs=["bold"], file=sys.stderr)
                                    continue
                                if sav:
                                    f = open(f"{fl.replace('.md', '_digest.md')}", "w")
                                    f.write(doc)
                                    f.close()
                else:
                    cprint("You have not been working on Obsidian notes for the past hour: enjoy your pause!💤", color="green", attrs=["bold"])
                    sys.exit(0)
                cprint("End of your digest!🎉", color="green", attrs=["bold"])
                sys.exit(0)

if __name__ == "__main__":
    main()
        


    
    