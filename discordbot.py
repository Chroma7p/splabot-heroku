# discord.pyの大事な部分をimport
from discord.ext import commands
from cogs.salmon_cog import SalmonCog
from cogs.regular_cog import RegularCog
from cogs.bankara_cog import BankaraCog
from cogs.weapon_cog import WeaponCog
import os
import discord
from dotenv import load_dotenv
import asyncio
load_dotenv(".env")

cogs = [SalmonCog,RegularCog,BankaraCog,WeaponCog]

APITOKEN= os.environ["SPLATOON_BOT_TOKEN"]


# botのオブジェクトを作成(コマンドのトリガーを!に)
bot = commands.Bot(command_prefix="/",intents=discord.Intents.all(), application_id=os.environ["SPLATOON_BOT_ID"])


# イベントを検知
@bot.event
# botの起動が完了したとき
async def on_ready():
    await bot.tree.sync()
    print("Hello!")  # コマンドラインにHello!と出力


async def main():
    # コグのフォルダ
    cogfolder = "cogs."
    # そして使用するコグの列挙(拡張子無しのファイル名)
    cogs = ["bankara_cog", "regular_cog", "salmon_cog" ,"weapon_cog","x_cog","now_cog","event_cog"]

    for c in cogs:
        await bot.load_extension(cogfolder + c)

    # start the client
    async with bot:
        await bot.start(APITOKEN)

asyncio.run(main())