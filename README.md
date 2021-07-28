# Discord-bot

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

Step 2. Set up your virtual environment with pipenv

```
$ pip install pipenv
$ pipenv install
```

Step 3. Set up your discord bot token

```
$ pipenv run dotenv set BOT_TOKEN YOUR_TOKEN
```

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

Step 2. Set up your virtual environment with pipenv
```
$ pip install pipenv
$ pipenv install --dev
```

Step 3. Reformat the coding style via [black](https://github.com/psf/black)
```
pipenv run black . 
```

Step 4. Check the coding style again via [black](https://github.com/psf/black) and [flake8](https://github.com/PyCQA/flake8)
```
pipenv run black . --check
pipenv run flake8 --max-line-length=88 .
```

## Authors
[Allen Wu](https://github.com/allen91wu)

