from discord.ext import commands, tasks
from discord import app_commands
import discord
from cogs.util.get_now_info import maketext


class NowCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Cogが読み込まれた時に発動
    @commands.Cog.listener()
    async def on_ready(self):
        print("NowCog on ready!")

    # コマンドの記述
    @app_commands.command(name="now", description="現在の各ルールの情報を表示します。")
    async def now(self, interaction: discord.Interaction):
        try:
            txt = maketext()
        except Exception as e:
            print(e)
            txt = "情報の取得に失敗しました"
        await interaction.response.send_message(txt)


# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(NowCog(bot))
