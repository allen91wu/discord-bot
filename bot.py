# Python 3.9.2 64-bit
import discord
from discord.ext import commands
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
    channel=bot.get_channel(824585823059574784)
    await channel.send(f'{member}join!')
# send message notice member join in discord

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
# print member leave in terminal

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(824585823059574784)
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

bot.run('ODI0NTY0MDQzMTU4MjU3Njk0.YFxNGw.3ApQrtk6_MSCnmQ5IPPR4Iwn-Og')