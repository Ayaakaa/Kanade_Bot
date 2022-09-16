import aiohttp

from utility.apps.sekai.api_functions import (get_sekai_user_api, get_sekai_cards_info_api)

#json
async def get_user_game_data(import_id: int, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['userid', 'name', 'deck', 'rank']
    if path in path_list:
        result = api['user']['userGamedata'][path]
        return result    
    else: 
        return None

async def get_user_profile(import_id: int, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['userid', 'word', 'twitterId', 'profileImageType']
    if path in path_list:
        result = api['userProfile'][path]
        return result    
    else: 
        return None

async def get_user_decks(import_id: int, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['leader', 'subLeader', 'member1', 'member2', 'member3', 'member4', 'member5' ]
    if path in path_list:
        result = api['userDecks'][0][path]
        return result    
    else: 
        return None  

async def get_user_cards(import_id: int, index: int, path: str, session: aiohttp.ClientSession):
    api = await get_sekai_user_api(import_id, session)
    path_list = ['cardId', 'level', 'masterRank', 'specialTraningStatus', 'defaultImage']
    if path in path_list:
        result = api['userCards'][index][path]
        return result    
    else: 
        return None  
    
#img
async def get_user_profile_pic(import_id: int, char_id: int, session: aiohttp.ClientSession):
    api = await get_sekai_cards_info_api(session)
    for char in api:
        if char['id'] == char_id:
            asset_bundle_name = char['assetBundleName']
            
    status_convert = {
        'original': 'normal',
        'special_training': 'after_training'
    }
    
    status = await get_user_cards(import_id, 0, 'defaultImage', session)
    status = status_convert[status]

    img_url = f'https://asset.pjsekai.moe/startapp/thumbnail/chara/{asset_bundle_name}_{status}.png'
    
    return img_url