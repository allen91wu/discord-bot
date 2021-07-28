import discord  # noqa: F401
from discord.ext import commands
from core.classes import Cog_Extension
import json

with open('setting.json', 'r', encoding='utf8') as jfile:
    jdata = json.load(jfile)


class React(Cog_Extension):
    @commands.command()
    async def sayd(self, ctx, *, msg):
        await ctx.message.delete()
        await ctx.send(msg)

    @commands.command()
    async def clean(self, ctx, num: int):
        await ctx.channel.purge(limit=num+1)


def setup(bot):
    bot.add_cog(React(bot))
