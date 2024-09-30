from discord.ext import commands, tasks
from discord import app_commands
import discord
from cogs.util.get_salmonrun_info import maketext
from datetime import datetime, timedelta, timezone
from cogs.notif_channel import channels

tz_jst = timezone(timedelta(hours=9))


class SalmonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels = channels
        self.notif.start()
        txt, self.next = maketext()

    # Cogが読み込まれた時に発動

    @commands.Cog.listener()
    async def on_ready(self):
        print("SalmonCog on ready!")
        await self.update_presence()

    async def update_presence(self):
        print(f"update_presence {self.next}")
        try:
            now = datetime.now(tz=tz_jst)
            time_for_next = self.next - now
            txt = f"[あと{time_for_next.seconds//3600+time_for_next.days*24}時間]{self.next.strftime('%d日%H:%M')}まで サーモンラン"
            print(txt)
            await self.bot.change_presence(activity=discord.Game(name=txt))
        except Exception as e:
            print(e)

    # コマンドの記述
    @app_commands.command(
        name="salmon", description="現在のサーモンランの情報を表示します。"
    )
    async def salmon(self, interaction: discord.Interaction):
        txt, self.next = maketext()
        await interaction.response.send_message(txt)

    @tasks.loop(minutes=3)
    async def notif(self):
        now = datetime.now(tz=tz_jst)
        if self.next < now:
            txt, self.next = maketext()
            if not self.next:
                return
            for channel_id in self.channels:
                channel = self.bot.get_channel(channel_id)
                await channel.send(txt)
        await self.update_presence()

    @app_commands.command(name="notif_set", description="通知設定を追加します。")
    async def notif_set(self, interaction: discord.Interaction):
        self.channels.add(interaction.channel.id)
        await interaction.response.send_message("通知設定を追加しました！")

    @app_commands.command(name="notif_unset", description="通知設定を削除します。")
    async def notif_unset(self, interaction: discord.Interaction):
        self.channels.remove(interaction.channel.id)
        await interaction.response.send_message("通知設定を削除しました！")

    @app_commands.command(name="notif_check", description="通知設定を確認します。")
    async def notif_check(self, interaction: discord.Interaction):
        txt = f"{self.next}\n"
        for channel in self.channels:
            txt += f"{channel}\n"
        await interaction.response.send_message(txt)


# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(SalmonCog(bot))
