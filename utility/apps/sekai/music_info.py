#musics
async def get_music_title(music_id):
    from utility.apps.sekai.api_functions import get_sekai_musics_api
    music_api = await get_sekai_musics_api()
    music_title = music_api[2]['title']
    return music_title

async def get_music_lyricist(music_id):
    from utility.apps.sekai.api_functions import get_sekai_musics_api
    music_api = await get_sekai_musics_api()
    music_lyricist = music_api[2]['lyricist']
    return music_lyricist

async def get_music_composer(music_id):
    from utility.apps.sekai.api_functions import get_sekai_musics_api
    music_api = await get_sekai_musics_api()
    music_composer = music_api[2]['composer']
    return music_composer

async def get_music_arranger(music_id):
    from utility.apps.sekai.api_functions import get_sekai_musics_api
    music_api = await get_sekai_musics_api()
    music_arranger = music_api[2]['arranger']
    return music_arranger

async def get_music_published_time(music_id):
    from utility.apps.sekai.api_functions import get_sekai_musics_api
    music_api = await get_sekai_musics_api()
    music_published_time = music_api[2]['publishedAt']
    return music_published_time

async def get_music_asset_name(music_id):
    from utility.apps.sekai.api_functions import get_sekai_musics_api
    music_api = await get_sekai_musics_api()
    music_asset_name = music_api[2]['assetbundleName']
    return music_asset_name
#music_difficulties

#music_vocals