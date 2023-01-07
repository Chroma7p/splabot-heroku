from discord.ext import commands,tasks
from get_regular_info import maketext

class RegularCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # コマンドの記述
    @commands.command()
    async def regular(self, ctx):
        txt=maketext()
        await ctx.send(txt)



# Cogとして使うのに必要なsetup関数
def setup(bot):
    print("RegularCog OK")
    return bot.add_cog(RegularCog(bot))
