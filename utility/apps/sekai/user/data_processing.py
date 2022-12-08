import aiohttp
import time
import discord
from discord import channel
from utility.apps.sekai.api_functions import (get_sekai_area_items_level_info_api, get_sekai_cards_info_api,
                                              get_sekai_characters_info_api,
                                              get_sekai_user_api,
                                              get_sekai_area_items_info_api,
                                              get_sekai_area_items_level_info_api,
                                              get_sekai_virtual_live_api_tw,
                                              get_sekai_virtual_live_api_jp)
from data.channel_list import channel_list
from utility.utils import defaultEmbed

#json
async def get_user_game_data(import_id: str, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['userId', 'name', 'deck', 'rank']
    if path in path_list:
        result = api['user']['userGamedata'][path]
        return result    

async def get_user_profile(import_id: str, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['userId', 'word', 'twitterId', 'profileImageType']
    if path in path_list:
        result = api['userProfile'][path]
        return result    
    
async def get_user_decks(import_id: str, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['leader', 'subLeader', 'member1', 'member2', 'member3', 'member4', 'member5' ]
    if path in path_list:
        result = api['userDecks'][0][path]
        return result    

async def get_user_area_items(import_id: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    api2 = await get_sekai_area_items_info_api(session)
    api3 = await get_sekai_area_items_level_info_api(session)
    embed_list = []
    area_items = api['userAreaItems']
    for item in area_items:
        item_id = item['areaItemId']
        item_level = item['level']
        for thing in api3:
            if item_id == thing['areaItemId'] and item_level == thing['level']:
                sentence = thing['sentence']
                #format sentence
                if sentence.count('。') == 1:
                    part1, part2 = sentence.split('<color=')
                    part2_1, part2_2 = part2.split('">')
                    part2_2_1, part2_2_2 = part2_2.split('</color')
                    sentence = f'{part1}{part2_2_1}。'
                    
                elif sentence.count('。') == 2:
                    sentence = sentence.rstrip(sentence[-1])
                    part1, part2 = sentence.split('>。')
                    
                    part1_1, part1_2 = part1.split('<color=')
                    part1_2_1, part1_2_2 = part1_2.split('">')
                    part1_2_2_1, part1_2_2_2 = part1_2_2.split('</color')
                    sentence1 = f'{part1_1}{part1_2_2_1}。'
                    
                    part2_1, part2_2 = part2.split('<color=')
                    part2_2_1, part2_2_2 = part2_2.split('">')
                    part2_2_2_1, part2_2_2_2 = part2_2_2.split('</color')
                    sentence2 = f'{part2_1}{part2_2_2_1}。'
                    
                    sentence = f'{sentence1}\n{sentence2}'
                    
        for thing in api2:
            if item_id == thing['id']:
                name = thing['name']
                asset_bundle_name = thing['assetbundleName']
                img = f'https://storage.sekai.best/sekai-assets/areaitem/{asset_bundle_name}_rip/{asset_bundle_name}.webp'
                embed = defaultEmbed(title=name, description= f'**等級：{item_level}**\n{sentence}')
                embed.set_thumbnail(url=img)
        embed_list.append(embed)        
    return embed_list
        

async def get_user_cards(import_id: str, index, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['cardId', 'level', 'masterRank', 'specialTraningStatus', 'defaultImage']
    if index == None:
        result = api['userCards']
    elif path in path_list and index != None:
            result = api['userCards'][index][path]
    return result    

#img
async def get_user_profile_pic(import_id: str, card_id: int, session: aiohttp.ClientSession):
    api = await get_sekai_cards_info_api(session)
    for card in api:
        if card['id'] == card_id:
            asset_bundle_name = card.get('assetbundleName')
            
    status_convert = {
        'original': 'normal',
        'special_training': 'after_training'
    }
    
    cards = await get_user_cards(import_id, None, 'N/A', session)
    for card in cards:
        if card_id == card['cardId']:
            default_image = card['defaultImage']
    status = status_convert[default_image]

    img_url = f'https://asset.pjsekai.moe/startapp/thumbnail/chara/{asset_bundle_name}_{status}.png'
    
    return img_url

async def get_profile_img(card_id: int, session: aiohttp.ClientSession):
    api = await get_sekai_cards_info_api(session)
    api2 = await get_sekai_characters_info_api(session)
    for card in api:
        if card['id'] == card_id:
            character_id = card['characterId']
            support_unit = card['supportUnit'] 
            if support_unit == 'none': 
                for char in api2:
                    if char['id'] == character_id: 
                        unit = char['unit']
            else:       
                unit = support_unit
    
    path_convert= {
        'light_sound': 'img_story_kyoshitsu',
        'school_refusal': 'img_story_daremoinai',
        'idol': 'img_story_stage',
        'street': 'img_story_street',
        'theme_park': 'img_story_wonderLand'
    }
    
    if unit == 'piapro':
        return None
    path = path_convert[unit]
    
    url =  f'https://gitlab.com/pjsekai/sprites/-/raw/master/{path}.png'
    
    return url
    
#character level
async def get_user_character_level(import_id: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    result = api['userCharacters']
    return result    

async def get_current_virtual_live_tw(session: aiohttp.ClientSession):
    api = await get_sekai_virtual_live_api_tw(session)
    for thing in api:
        virtual_live_start_time = thing['startAt']
        virtual_live_end_time = thing['endAt']
        current_time = time.time()
        if current_time > virtual_live_start_time / 1000 and current_time < virtual_live_end_time / 1000:
            return thing
    else: return None

async def virtual_live_ping_tw(bot, session: aiohttp.ClientSession):
    current_virtual_live = await get_current_virtual_live_tw(session)
    if current_virtual_live != None:
        for thing in current_virtual_live['virtualLiveSchedules']:
            name = current_virtual_live['name']
            virtual_live_start_time = thing['startAt']
            current_time = time.time()
            if int(current_time) + 300 in  range(virtual_live_start_time - 100, virtual_live_start_time + 100):
                embed = defaultEmbed(title= f'虛擬 Live 即將開始', description=f'{name} 將於五分鐘後開始')
                for thing in channel_list:           
                    channel = bot.get_channel(int(thing))
                    await channel.send(embed=embed)
        else: pass
    else: pass


async def get_current_virtual_live_jp(session: aiohttp.ClientSession):
    api = await get_sekai_virtual_live_api_jp(session)
    for thing in api:
        virtual_live_start_time = thing['startAt']
        virtual_live_end_time = thing['endAt']
        current_time = time.time()
        if current_time > virtual_live_start_time / 1000 and current_time < virtual_live_end_time / 1000:
            return thing
    else: return None

async def virtual_live_ping_jp(bot, session: aiohttp.ClientSession):
    current_virtual_live = await get_current_virtual_live_jp(session)
    if current_virtual_live != None:
        for thing in current_virtual_live['virtualLiveSchedules']:
            name = current_virtual_live['name']
            virtual_live_start_time = thing['startAt']
            current_time = time.time()
            if int(current_time) + 300 in  range(virtual_live_start_time - 100, virtual_live_start_time + 100):
                embed = defaultEmbed(title= f'虛擬 Live 即將開始', description=f'{name} 將於五分鐘後開始')
                for thing in channel_list:           
                    channel = bot.get_channel(int(thing))
                    await channel.send(embed=embed)
        else: pass
    else: pass
    
async def get_user_music(import_id: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    api = api['userMusic']
    
    for thing in api:
        music_id = thing['musicId']
        difficulties = thing['userMusicDifficultyStatuses']
        
        for difficulty in difficulties:
            music_results= difficulty['userMusicResults']
            if len(music_results) == 0: pass
            else:
                music_result_solo ={}
                music_results[0]
                
                    
        