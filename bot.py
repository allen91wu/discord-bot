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

@bot.event
async def on_member_join(member):
    channel=bot.get_channel(817391687991164960)
    await channel.send(f'{member}join!')
# send message notice member join in discord

@bot.event
async def on_member_remove(member):
    print(f'{member}leave!')
# print member leave in terminal

@bot.event
async def on_member_remove(member):
    channel=bot.get_channel(817391687991164960)
    await channel.send(f'{member}leave!')
# send message notice member leave in discord

bot.run('ODI0NTY0MDQzMTU4MjU3Njk0.YFxNGw.3ApQrtk6_MSCnmQ5IPPR4Iwn-Og')