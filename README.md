# Discord-bot

## Prerequisite
- [Python3](https://www.python.org/downloads/)
- [discord.py](https://github.com/Rapptz/discord.py)

## Function
- Meme pictures sender
- Chat bot
- Ping
- Remove messages
- Echo messages

## Usage (Windows & Linux)

Step 1. Download the repo
```
$ git clone https://github.com/allen91wu/discord-bot
$ cd discord-bot
```

Step 2. Set up the virtual environment

```
$ pip install pipenv
$ pipenv install
```
- [pipenv](https://github.com/pypa/pipenv): for dependency management

Step 3. Set up your discord bot token

```
$ pipenv run dotenv set BOT_TOKEN YOUR_TOKEN
```

- [dotenv](https://github.com/theskumar/python-dotenv)
- [Discord developer portal](https://discord.com/developers/applications)

Step 4. Implement the bot server

```
$ pipenv run python main.py
```

## Development
Step 1. Download the repo
```
$ git clone https://github.com/allen91wu/discord-bot
$ cd discord-bot
```

Step 2. Set up the virtual environment
```
$ pip install pipenv
$ pipenv install --dev
```

Step 3. Set up your discord bot token
```
$ pipenv run dotenv set BOT_TOKEN YOUR_TOKEN
```

- [dotenv](https://github.com/theskumar/python-dotenv)
- [Discord developer portal](https://discord.com/developers/applications)

Step 4. Work on your new feature and make sure it can work

Step 5. Reformat the coding style
```
$ pipenv run black . 
```

Step 6. Check the coding style again
```
$ pipenv run black . --check
$ pipenv run flake8 .
```
Step 7. Run security check
```
$ pipenv check
```

- [black](https://github.com/psf/black)
- [flake8](https://github.com/PyCQA/flake8)

## Authors
[Allen Wu](https://github.com/allen91wu)

