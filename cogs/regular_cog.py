from discord.ext import commands
from discord import app_commands
import discord
from get_regular_info import maketext

class RegularCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Cogが読み込まれた時に発動
    @commands.Cog.listener()
    async def on_ready(self):
        print('RegularCog on ready!')

    # コマンドの記述
    @app_commands.command(name="regular",description="現在のレギュラーマッチの情報を表示します。")
    async def regular(self, interaction:discord.Interaction):
        txt=maketext()
        await interaction.response.send_message(txt)



# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(RegularCog(bot))
