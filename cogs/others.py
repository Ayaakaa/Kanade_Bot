import random
from datetime import datetime
from random import randint

import discord
from data.user_data import morning, special
from discord import app_commands
from discord.ext import commands
from utility.utils import updateEmbed
from data.version import version

class OthersCog(commands.Cog, name='others'):
    
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name='embed', description='embed')
    @app_commands.rename(description='embed-description', cmd_1='cmd-1-name', cmd_1_des='cmd-1-description', cmd_2='cmd-2-name', cmd_2_des='cmd-2-description', cmd_3='cmd-3-name', cmd_3_des='cmd-3-description')
    @app_commands.checks.has_role('小雪團隊')
    async def update(self, interaction: discord.Interaction, description: str, cmd_1: str = '', cmd_1_des: str = '', cmd_2: str = '', cmd_2_des: str = '', cmd_3: str = '', cmd_3_des: str = ''):
        embed = updateEmbed(description=description,)
        if len(cmd_1) >= 1:
            embed.add_field(name=f'{cmd_1}', value=f'{cmd_1_des}', inline=False)
        if len(cmd_2) >= 1:
            embed.add_field(name=f'{cmd_2}', value=f'{cmd_2_des}', inline=False)
        if len(cmd_3) >= 1:
            embed.add_field(name=f'{cmd_3}', value=f'{cmd_3_des}', inline=False)
        await interaction.response.send_message(embed=embed)
        
async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(OthersCog(bot))