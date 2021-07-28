import discord  # noqa: F401
from discord.ext import commands


class Cog_Extension(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
