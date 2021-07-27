# Python 3.9.2 64-bit
import discord
from discord.ext import commands
import json
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN= os.getenv('BOT_TOKEN')

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
# print online in terminal

@bot.command()
async def helpme(ctt):
    await ctt.send(jdata['explain'])
    print('sned a message')
# explain discord bot

@bot.command()
async def load(ctx,extension):
    bot.load_extension(f'cmds.{extension}')
    await ctx.send(f'loaded {extension} done.')
    print('sned a message')

@bot.command()
async def unload(ctx,extension):
    bot.unload_extension(f'cmds.{extension}')
    await ctx.send(f'un-loaded {extension} done.')
    print('sned a message')

@bot.command()
async def reload(ctx,extension):
    bot.reload_extension(f'cmds.{extension}')
    await ctx.send(f're-loaded {extension} done.')
    print('sned a message')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')


if __name__=="__main__":
    BOT_TOKEN= os.getenv('BOT_TOKEN')
    bot.run(BOT_TOKEN)