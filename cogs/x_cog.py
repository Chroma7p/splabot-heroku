from discord.ext import commands,tasks
from discord import app_commands
import discord
from get_x_info import maketext

class XCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Cogが読み込まれた時に発動
    @commands.Cog.listener()
    async def on_ready(self):
        print('XCog on ready!')

    # コマンドの記述
    @app_commands.command(name="xmatch",description="現在のXマッチの情報を表示します。")
    async def xmatch(self, interaction:discord.Interaction):
        txt=maketext()
        await interaction.response.send_message(txt)
    




# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(XCog(bot))
