import json
import random

import discord  # noqa: F401
from discord.ext import commands

from core.classes import Cog_Extension

with open("setting.json", "r", encoding="utf8") as jfile:
    jdata = json.load(jfile)


class Event(Cog_Extension):
    @commands.Cog.listener()
    async def on_message(self, msg):
        keyword = jdata["keyword"]
        if msg.content in keyword and msg.author != self.bot.user:
            await msg.channel.send("爛")
        if msg.content == "機器人":
            await msg.channel.send("你好吵")
        if msg.content == "要不要吃烤肉":
            await msg.channel.send("好啊我想吃")
        if msg.content == "走啊":
            await msg.channel.send("哪次不去了")
        if msg.content == "餓":
            await msg.channel.send("吃飯")
        if msg.content == "早安":
            await msg.channel.send("早安阿")
        if msg.content == "閉嘴機器人":
            await msg.channel.send("你他媽才閉嘴")
        if msg.content == "要一起想像嗎":
            await msg.channel.send("你他媽才葉宜")
        if msg.content.endswith("郭"):
            random_kuo = random.choice(jdata["kuoword"])
            await msg.channel.send(random_kuo)
        if msg.content.endswith(".") and msg.author != self.bot.user:
            random_pictures_number = str(random.randrange(146), ".jpg")
            link_title = "https://allen91wu.github.io/discord-bot/meme/meme_"
            await msg.channel.send(link_title, random_pictures_number)


def setup(bot):
    bot.add_cog(Event(bot))
