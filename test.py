# Python 3.8
import os

from discord.ext import commands

bot = commands.Bot(command_prefix="[")

for filename in os.listdir("./cmds"):
    if filename.endswith(".py"):
        bot.load_extension(f"cmds.{filename[:-3]}")

if __name__ == "__main__":
    print("Sucessfully loaded")
