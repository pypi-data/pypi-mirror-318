<div align="center">
<h1>obsidian-digest</h1>
<h2>Superpower your notes with Gemini 2</h2>
</div>
<br>
<div align="center">
    <img src="https://raw.githubusercontent.com/AstraBert/obsidian-digest/main/logo.png" alt="PdfItDown Logo">
</div>

🧠 **obsidian-digest** is a tool to superpower your [Obsidian](https://obsidian.md/) notes with LLM-based suggestions and considerations on style and contents!

### ✅ Pre-requisites

- (**mandatory**) an [Obsidian](https://obsidian.md/) account and the Desktop application installed
- (**mandatory**) [`git` toolset](https://git-scm.com/docs)
- (**mandatory**) A Gemini [API key](https://aistudio.google.com/apikey)
- (**optional**) [`python`] 3.10 or following versions
- (**optional**) [`conda`](https://docs.conda.io/projects/conda/en/latest/user-guide/getting-started.html) package manager
- (**optional**) [`docker`](https://www.docker.com/) and [`docker compose`](https://docs.docker.com/compose/)
- (**optional**) [Discord](https://discord.com/) and a Discord account

### 🤝 Common Steps for Installation

Clone this GitHub repository and access it:

```bash
git clone https://github.com/AstraBert/obsidian-digest.git
cd obsidian-digest
```

Move `.env.example` to `.env` and fill in the variables there contained according to what reported in your preferred installation procedure:

```bash
mv .env.example .env
```

### 📦 1. Python Package

> _Pre-requistes: `python` 3.10 or following versions_

If you wish to install `obsidian-digest` as a Python package, you can do so just by running:

```bash
python3 -m pip install obsidian_digest
```

When the installation is complete, you can use the CLI tool following these instructions:

```
usage: obsidian_digest [-h] -d DIRECTORY [-a] -k APIKEY [-s]

options:
  -h, --help            show this help message and exit
  -d DIRECTORY, --directory DIRECTORY
                        Directory containing Obsidian notes for which to produce the digest
  -a, --allfiles        Produce the digest for all the files in the directory, and not only for those modified in the last hour
  -k APIKEY, --apikey APIKEY
                        Provide your Google Gemini API key either as a path to your .env file containing the
                        GOOGLE_API_KEY variable, the name of the environmental variable under which the key is stored
                        or the key itself (the first two methods are suggested)
  -s, --save            Save the digest as a Markdown File in your Obsidia vault
```

Example usages could be:

```bash
# Get the digest for all files, save the digests and pass the API key as a .env file
obsidian_digest -k ./envs/.env -d obsidian/notes/ -a -s
# Get the digest only for the files you modified in the last hour, pass the API key as an environmental variable, do not save the digests
obsidia_digest -k GEMINI_API -d obsidian/notes/
```

We advise to use the `.env` file [template](./.env.example) from this repository, filling in only the variable `GOOGLE_API_KEY` with your API key. 

### 🤖 2. Discord Bot - Native Code

> _Pre-requistes: `python` 3.10 or following versions **or** `conda` package manager_

From the repository that you cloned, you can create a python virtual environment and install all the dependencies in [`requirements.txt`](./requirements.txt): 

```bash
python3 -m venv virtualenv
source virtualenv/bin/activate
python3 -m pip install -r requirements.txt
```

**Alternatively**, if you have `conda`, you can create a conda environment named `obsidian-digest` from the [`conda_environment.yaml`](./conda_environment.yaml) configuration file in this repository: 

```bash
conda env create -f conda_environment.yaml
conda activate obsidian-digest
```

Now you should modify your `.env` file filling all the variables. If you don't know how to create a Discord bot and get its token and the channel ID, here is a quick breakdown:

1. Go to [Discord](https://discord.com/) and create an account (or log into yours, if you already have one)
2. Create a new server by clicking on "Add a server" (a big green "+" button) and name it as you want
3. Go to [Discord developers portal](https://discord.com/developers/applications) and click on "New application"
4. Name your application, than save the changes and click on "Bot", on the left
5. There you will get the chance to name your bot and copy its token: paste it under the `discord_bot` field in your [`.env`](./.env.example) file.
6. After that, go on OAuth2 > URL generator and generate a URL that you will paste in your navigation bar, to add the bot to your newly created server.
7. In the `channel_id` field in your [`.env`](./.env.example) file, insert the **last number** that is displayed in your server's **#general channel url** when you open it on the web.

Once you are done with all the set-up, simply run (from inside the virtual environment or from inside the conda environment):

```bash
python3 scripts/native/bot.py
```

The bot will send a digest for all the files you modified in the hour before its activation, and it will keep sending hourly digest on the channel it was linked to.

### 🐋 3. Discord Bot - Docker Compose

Using `docker compose` can make deployment easier, because it does not need any environment-setting steps, apart from setting the variables in the [`.env`](./.env.example) file as in option 2.

You can now run:

```bash
docker compose up
```

And an image with all the required dependencies and [scripts](./scripts/docker/) will be built on the fly and used as a base for a container, in which our Discord bot will run. On the user side, the bot works in the same way as the one built from native code. 

### ⚙️ How does it work?

The overall workflow is pretty simple:

- obsidian-digest finds the notes you worked on in the last hour under your vault path that you specified either as an option to the CLI tool or from the `NOTES_PATH` in the .env file
- These files are uploaded to Gemini API, along with a prompt that asks Gemini to create a JSON answer, that contains style suggestions, content suggestions and overall considerations
- Gemini's response is parsed and reconstructed into a message for each file
- The final digest is then streamlined to the terminal (if you used the CLI tool) or to Discord (if you used one of the two Discord bot solutions)

### 🎁 Contributing

Contributions are always welcome!

Find contribution guidelines at [CONTRIBUTING.md](https://github.com/AstraBert/obsidian-digest/tree/main/CONTRIBUTING.md)

### 💜 License and Funding

This project is open-source and is provided under an [MIT License](https://github.com/AstraBert/obsidian-digest/tree/main/LICENSE).

If you found it useful, please consider [funding it](https://github.com/sponsors/AstraBert).