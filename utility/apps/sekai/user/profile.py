import aiohttp

import discord
from discord import Embed, app_commands, embeds
from discord.app_commands import Choice
from discord.ext import commands

from utility.apps.sekai.time_formatting import format_date_jp
from utility.apps.sekai.user.data_processing import (get_profile_img,
                                                     get_user_decks,
                                                     get_user_game_data,
                                                     get_user_profile,
                                                     get_user_profile_pic)
from utility.utils import defaultEmbed


async def user_profile(import_id: int, session: aiohttp.ClientSession):
    if import_id == await get_user_game_data(import_id, 'userId', session):
        name = await get_user_game_data(import_id, 'name', session)
        user_id = import_id
        rank = await get_user_game_data(import_id, 'rank', session)
        word = await get_user_profile(import_id, 'word', session)
        leader_id = await get_user_decks(import_id, 'leader', session)
        tl_url = await get_user_profile_pic(import_id, leader_id, session)  
        img_url = await get_profile_img(leader_id, session)  
        if word == None or len(word) < 1: word = 'none'
        seconds = int((1600218000000 + user_id / 2 ** 22) + 25200000)
        creation_date = await format_date_jp (seconds)
        
        embed = defaultEmbed(title=f'**{name}**', description=f'「{word}」')
        embed.set_thumbnail(url=tl_url)
        embed.set_image(url=img_url)
        embed.add_field(name=f'等級：', value=rank, inline=False)
        embed.add_field(name=f'玩家 ID：', value=f'`{user_id}`', inline=False)
        embed.add_field(name=f'創建日期：', value=f'{creation_date}', inline=False)
        
        return embed

