import discord  # noqa: F401
from core.classes import Cog_Extension
from discord.ext import commands


class Main(Cog_Extension):
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"{round(self.bot.latency*1000)}(ms)")
        print("sned a message")

    # test send ping float


def setup(bot):
    bot.add_cog(Main(bot))
