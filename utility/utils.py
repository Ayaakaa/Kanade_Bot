import logging
import discord
from datetime import datetime

from data.version import version

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
log = logging


def defaultEmbed(title: str = '', description: str = ''):
    embed = discord.Embed(title=title, description=description, color=0xBB6688)
    return embed

def loadingEmbed(text: str, img: str, thumbnail: bool):
            embed = defaultEmbed(title = f'**正在獲取{text}資料...**',
                             description = f'獲取資料需時，請耐心等候')
            if thumbnail == True:
                embed.set_thumbnail(url = img)
            else:
                embed.set_image(url = img)
            return embed     

def updateEmbed(description: str = ''):
    embed = discord.Embed(title=f'**奏寶 v{version}**', description=description, color=0xBB6688)
    embed.set_author(name="奏寶", url="https://github.com/Ayaakaa/kanade_bot",
                         icon_url="https://i.imgur.com/oXEl8tP.jpg")
    embed.set_image(url="https://i.imgur.com/1SJ6Y0Y.jpg")
    embed.set_footer(text=f"奏寶 - by 綾霞 Ayaakaa",
                     icon_url="https://avatars.githubusercontent.com/u/80079457?v=4")
    return embed

def errEmbed(title: str = '', message: str = ''):
    embed = discord.Embed(title=title, description=message, color=0xfc5165)
    embed.set_footer(text=f"如果你認為這是一個 BUG，歡迎私訊綾霞 ayaakaa#1127")
    return embed

def log(is_system: bool, is_error: bool, log_type: str, log_msg: str):
    now = datetime.now()
    today = datetime.today()
    current_date = today.strftime('%Y-%m-%d')
    current_time = now.strftime("%H:%M:%S")
    system = "SYSTEM"
    if not is_system:
        system = "USER"
    if not is_error:
        log_str = f"<{current_date} {current_time}> [{system}] ({log_type}) {log_msg}"
    else:
        log_str = f"<{current_date} {current_time}> [{system}] [ERROR] ({log_type}) {log_msg}"
    with open('log.txt', 'a+', encoding='utf-8') as f:
        f.write(f'{log_str}\n')
    return log_str

def divide_chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
class Convert:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Convert({self.name!r})'       
    def convert(value):
        return Convert(value.decode('utf-8'))
