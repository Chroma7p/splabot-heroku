from discord.ext import commands,tasks
from get_salmonrun_info import maketext
from datetime import datetime,timedelta,timezone


tz_jst = timezone(timedelta(hours=9))



class SalmonCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.channels=set()
        self.notif.start()
        txt,self.next=maketext()

    # コマンドの記述
    @commands.command()
    async def salmon(self, ctx):
        txt,self.next=maketext()
        await ctx.send(txt)

    @tasks.loop(minutes=3)
    async def notif(self):
        now=datetime.now(tz=tz_jst)

        if self.next < now:

            for channel in self.channels:
                txt,self.next=maketext()
                await channel.send(txt)
            print(f"notif fire:{now}")
            print(f"next:{self.next}")

                
        
    @commands.command()
    async def notif_set(self,ctx):
        self.channels.add(ctx.channel)
        await ctx.send("通知を設定しました！")

    @commands.command()
    async def notif_unset(self,ctx):
        self.channels.remove(ctx.channel)
        await ctx.send("通知設定を削除しました！")

    @commands.command()
    async def notif_check(self,ctx):
        txt=f"{self.next}\n"
        for channel in self.channels:
            txt+=f"{channel}\n"
        await ctx.send(txt)

    


# Cogとして使うのに必要なsetup関数
def setup(bot):
    print("salmonCog OK")
    return bot.add_cog(SalmonCog(bot))
