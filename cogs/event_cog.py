from discord.ext import commands,tasks
from discord import app_commands
import discord
from get_event_info import maketext,get_next,makenotif
from datetime import datetime,timedelta,timezone
from cogs.notif_channel import channels

tz_jst = timezone(timedelta(hours=9))



class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels=channels
        self.notif.start()
        self.next=get_next()
        
        

    # Cogが読み込まれた時に発動
    @commands.Cog.listener()
    async def on_ready(self):
        print('EventCog on ready!')
            
    # コマンドの記述
    @app_commands.command(name="event",description="現在のイベントマッチの情報を表示します。")
    async def event(self, interaction:discord.Interaction):
        try:
            txt=maketext()
            await interaction.response.send_message(txt)
        except Exception as e:
            await interaction.response.send_message("情報の取得に失敗しました。")
            print(e)

    @tasks.loop(minutes=3)
    async def notif(self):
        now=datetime.now(tz=tz_jst)
        print(now,self.next)
        if self.next < now:
            txt,self.next=makenotif()
            if not self.next:
                return
            for channel_id in self.channels:
                channel= self.bot.get_channel(channel_id)
                await channel.send(txt)
            

    
    

# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(EventCog(bot))
