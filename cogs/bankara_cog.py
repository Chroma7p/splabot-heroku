from discord.ext import commands,tasks
from get_bankara_info import maketext

class BankaraCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # コマンドの記述
    @commands.command()
    async def open(self, ctx):
        txt=maketext(is_open=True)
        await ctx.send(txt)
    
    @commands.command()
    async def challenge(self, ctx):
        txt=maketext(is_open=False)
        await ctx.send(txt)




# Cogとして使うのに必要なsetup関数
def setup(bot):
    print("BankaraCog OK")
    return bot.add_cog(BankaraCog(bot))
