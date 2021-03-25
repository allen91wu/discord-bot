# Python 3.9.2 64-bit
import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")
# print online in terminal
@bot.event
async def on_member_join(member):
    print(f'{member}join!')
# print member join in terminal

bot.event
async def on_member_join(member):
    channel=bot.get_channel(int(jdata['general_channel']))
    await channel.send(f'{member}join!')
# send message notice member join in discord

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
# print member leave in terminal

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(int(jdata['general_channel']))
    await channel.send(f'{member}leave!')
# send message notice member leave in discord

@bot.command()
async def ping(ctx):
   await ctx.send(f'{round(bot.latency*1000)}(ms)')
# test send ping float

@bot.command()
async def 要不要吃烤肉(ctt):
   await ctt.send('好啊我想吃')
# test chat

@bot.command()
async def 走啊(ctt):
   await ctt.send('哪次不去了')
# test chat

bot.run(jdata['TOKEN'])
client.run(jdata['TOKEN'])