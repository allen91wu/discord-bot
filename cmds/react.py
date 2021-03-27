import discord
from discord.ext import commands
from core.classes import Cog_Extension
import random
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata=json.load(jfile)

class React(Cog_Extension):

    @commands.command()
    async def 要不要吃烤肉(self,ctt):
        await ctt.send('好啊我想吃')
        print('sned a message')
    # chat
    
    @commands.command()
    async def 走啊(self,ctt):
        await ctt.send('哪次不去了')
        print('sned a message')
    # chat

    @commands.command()
    async def 餓(self,ctt):
        await ctt.send('吃飯')
        print('sned a message')
    # chat

    @commands.command()
    async def 早安(self,ctt):
       await ctt.send('早安阿')
       print('sned a message')
    # chat

    @commands.command()
    async def 閉嘴機器人(self,ctt):
        await ctt.send('你他媽才閉嘴')
        print('sned a message')
    # chat

    @commands.command()
    async def 要一起想像嗎(self,ctt):
        await ctt.send('你他媽才葉宜')
        print('sned a message')
    # chat


def setup(bot):
    bot.add_cog(React(bot))