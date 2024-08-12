from discord.ext import commands
from discord import app_commands
import discord
from cogs.util.weapon import get_weapon_info, extract_weapon_types, filter_weapons
import random


class WeaponCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.weapons = get_weapon_info()
        self.weapon_types, self.sub_types, self.special_types = extract_weapon_types(
            self.weapons
        )

    # Cogが読み込まれた時に発動
    @commands.Cog.listener()
    async def on_ready(self):
        print("WeaponCog on ready!")

    # コマンドの記述
    @app_commands.command(name="gacha", description="ブキガチャを引きます(重複あり)。")
    @app_commands.describe(n="引く個数を選んでね")
    async def gacha(self, interaction: discord.Interaction, n: int = 1):
        if n > 10:
            n = 10
        elif n < 1:
            n = 1
        txt = ""
        for i in range(n):
            weapon = random.choice(self.weapons)
            txt += f"{str(weapon)}\n"

        await interaction.response.send_message(txt)

    @app_commands.command(name="shibari", description="縛りガチャを引きます。")
    async def shibari(self, interaction: discord.Interaction):
        try:
            shiba_type = random.randrange(3)
            if shiba_type == 0:
                shiba = random.choice(self.weapon_types)
                weapons = filter_weapons(self.weapons, weapon_type=shiba)
            elif shiba_type == 1:
                shiba = random.choice(self.sub_types)
                weapons = filter_weapons(self.weapons, sub_type=shiba)
            else:
                shiba = random.choice(self.special_types)
                weapons = filter_weapons(self.weapons, special_type=shiba)

            txt = f"縛りは{shiba}だよ！対象ブキはこちら！\n"
            for weapon in weapons:
                txt += f"{str(weapon)}\n"
        except Exception as e:
            txt = str(e)
        await interaction.response.send_message(txt)

    @app_commands.command(name="search", description="ブキの情報を検索します。")
    async def search(self, interaction: discord.Interaction, *, name: str):
        try:
            weapons = filter_weapons(self.weapons, sub_type=name, soft=True)
            weapons += filter_weapons(self.weapons, special_type=name, soft=True)
            weapons += [weapon for weapon in self.weapons if name in weapon.main]
            if len(weapons) == 0:
                txt = f"'***{name}***'で検索して何も見つからなかったよ…"
            txt = f"'***{name}***'で検索して{len(weapons)}件見つかったよ！\n"
            for weapon in weapons:
                txt += f"{str(weapon)}\n"
        except Exception as e:
            txt = str(e)
        return await interaction.response.send_message(txt)


# Cogとして使うのに必要なsetup関数
def setup(bot):
    return bot.add_cog(WeaponCog(bot))
