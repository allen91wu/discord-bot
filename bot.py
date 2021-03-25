import discord
from discord.ext import commands

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('ODI0NTY0MDQzMTU4MjU3Njk0.YFxNGw.RRrFOHRJuc5gYYcTXdLB-r4lVn0')