import discord  # noqa: F401
import requests
from bs4 import BeautifulSoup
from core.classes import Cog_Extension
from discord.ext import commands


def kktix_count(web):
    r = requests.get(web)
    soup = BeautifulSoup(r.text, "html.parser")
    ticket_count = soup.find("span", class_="info-count")
    return ticket_count.text


def kktix_all():
    individual = "個人票：" + kktix_count("https://pycontw.kktix.cc/events/2021-individual")
    corporate = "企業票：" + kktix_count("https://pycontw.kktix.cc/events/2021-corporate")
    reserved = "保留票：" + kktix_count("https://pycontw.kktix.cc/events/2021-reserved")
    combined = individual + "\n" + corporate + "\n" + reserved
    return combined


class Kktix(Cog_Extension):
    @commands.command()
    async def pycontw(self, ctx):
        warning = str("請等我幾秒鐘我正在抓資料，不要催我，人家會害羞，所以我說尊重呢？")
        await ctx.send(warning)
        combined = "PyCon TW 2021 目前售票狀況為：\n" + kktix_all()
        await ctx.send(combined)


def setup(bot):
    bot.add_cog(Kktix(bot))
