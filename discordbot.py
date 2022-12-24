# discord.pyの大事な部分をimport
from discord.ext import commands,tasks
import discord
import os
from cogs.salmon_cog import SalmonCog,maketext
import sys
import time

cogs = [SalmonCog]

APITOKEN= os.environ["SPLATOON_BOT_TOKEN"]


# botのオブジェクトを作成(コマンドのトリガーを!に)
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())


# イベントを検知
@bot.event
# botの起動が完了したとき
async def on_ready():
    for cog in cogs:
        await bot.add_cog(cog(bot))
    print("Hello!")  # コマンドラインにHello!と出力






# 起動
bot.run(APITOKEN)
