from discord.ext import commands,tasks
from discord import app_commands
import discord
from get_bankara_info import maketext

class BankaraCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Cogが読み込まれた時に発動
    @commands.Cog.listener()
    async def on_ready(self):
        print('BankaraCog on ready!')

    # コマンドの記述
    @app_commands.command(name="open",description="現在のバンカラマッチ(オープン)の情報を表示します。")
    async def open(self, interaction:discord.Interaction):
        txt=maketext(is_open=True)
        await interaction.response.send_message(txt)
    
    @app_commands.command(name="challenge",description="現在のバンカラマッチ(チャレンジ)の情報を表示します。")
    async def challenge(self, interaction:discord.Interaction):
        txt=maketext(is_open=False)
        await interaction.response.send_message(txt)




# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(BankaraCog(bot))
