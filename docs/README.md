# Discord-bot

It'a discord bot.

## Getting Started

### Prerequisites
- [Python3](https://www.python.org/downloads/)
- [discord.py](https://github.com/Rapptz/discord.py)

## Function
- Meme pictures sender
- Chat bot
- Ping
- Remove messages
- Echo messages

## Usage
Step 1. Download the repo
```sh
$ git clone https://github.com/allen91wu/discord-bot
$ cd ./discord-bot/discord-bot/
```

Step 2. Set up the virtual environment

```sh
$ pip install pipenv
$ pipenv install
```
- [pipenv](https://github.com/pypa/pipenv): for dependency management

Step 3. Set up your discord bot token

```sh
$ pipenv run dotenv set BOT_TOKEN YOUR_TOKEN
```

- [dotenv](https://github.com/theskumar/python-dotenv)
- [Discord developer portal](https://discord.com/developers/applications)

Step 4. Implement the bot server
```sh
$ pipenv run python discord-bot.py
```


## Contributing
See [Contributing](contributing.md)

## Authors
[Allen Wu](https://github.com/allen91wu)


Created from [Lee-W/cookiecutter-python-template](https://github.com/Lee-W/cookiecutter-python-template/tree/0.9.1) version 0.9.1
