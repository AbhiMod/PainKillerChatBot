from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram.types import ChatMember
from pyrogram import *
import asyncio
import psutil
import traceback
from pyrogram.types import *
from pymongo import MongoClient
import requests
import os, time
from datetime import datetime
import pytz
from gpytranslate import Translator
from gtts import gTTS
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from telegraph import upload_file
from pyrogram.types import InputMediaPhoto
import pyrogram
from pyrogram.types import Message
from pyrogram.errors import FloodWait
from pytgcalls import PyTgCalls
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import (
    AlreadyJoinedError,
    NoActiveGroupCall,
    TelegramServerError,
)
from youtubesearchpython import VideosSearch
import yt_dlp
from pyrogram.handlers import MessageHandler
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded
from pytgcalls import PyTgCalls, StreamType
from pytgcalls.exceptions import AlreadyJoinedError, NoActiveGroupCall, TelegramServerError
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from pyrogram.raw import functions
from pyrogram.raw.types import InputChannelEmpty
from datetime import datetime
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re
from typing import Dict, Union
from PIL import ImageDraw, Image, ImageFont, ImageChops
from pyrogram import *
from pyrogram.types import *

API_ID = "6435225"
API_HASH = "4e984ea35f854762dcde906dce426c2d"
STRING = os.environ.get("STRING", "")
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srv://kuldiprathod2003:kuldiprathod2003@cluster0.wxqpikp.mongodb.net/?retryWrites=true&w=majority")
SUDOERS = 6204761408
client = Client(STRING, API_ID, API_HASH)
AMTAGS= [
    "ᴏɪɪ ᴀᴍʙᴏᴛ ᴋᴏ ᴛᴀɢ ᴍᴀᴛᴛ ᴋᴀʀᴏ ᴡᴏ ᴀʙ ʙᴜꜱʏ ʜᴇ",
    "𝓠 𝔂𝓪𝓪𝓭 𝓚𝓪𝓻𝓻𝓱𝓮 𝓱𝓸 𝓐𝓜𝓑𝓞𝓣 𝓚𝓸",
    "𝘼𝙈𝘽𝙊𝙏 𝘾𝙖𝙡𝙡 𝙋𝙚 𝙃𝙚 𝘼𝙗 𝙒𝙤 𝙈𝙚𝙧𝙚 𝙎𝙖𝙩𝙝",
    "ᴋᴏɪ ɪꜱᴋᴏ @AM_YTBOTT ɢꜰ ᴅɪʟᴀᴅᴏ..😢😢😢",
    "𝘼𝙗 𝘼𝙗 𝙊𝙛𝙡𝙞𝙣𝙚 𝙂𝙖𝙮𝙖 𝙒𝙤 𝙅𝙖𝙤 𝘾𝙖𝙡𝙡 𝙆𝙖𝙧𝙡𝙤 𝙖𝙖𝙟𝙖𝙮𝙖 𝙜𝙖 𝙊𝙣𝙡𝙞𝙣𝙚 😜😜"
]

AAA = [
    "Nahi Me To Cute Mikashaa hu ☺️😊",
    "Tumko Kya Lagta He 😢😒",
    "Nahi U Bot 😂",
    "Are Kuch V 😳😂",
    "Puch Lo AMBOT Se Me Kon Hu 🙈",
    "Me Insaan Hu Reee Aaj Tumko Pitna He sayad 😏",
]
PING_IMG_URL = "https://graph.org/file/8b7ebf25c70040bd26485.jpg"
REPO = """ᴍɪᴋᴀsʜᴀᴀ ᴀɪ⌫
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎ ᴀᴍʙᴏᴛ:</u>

𝗥𝗘𝗣𝗢 ❥︎ [𝗥𝗘𝗣𝗢](t.me/About_AMBot)

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ [ɢʙᴀɴꜱ ʟᴏɢꜱ](https://t.me/Logs_Gban)

𝗢𝗪𝗡𝗘𝗥 ❥︎ [ᴀᴍʙᴏᴛ](https://t.me/AM_YTBOTT)"""
HELP = """ʜᴇʀᴇ ɪꜱ ᴄᴍᴅꜱ ꜰᴏʀ ᴛᴀɢᴀʟʟ\nᴜꜱᴇ ᴄᴍᴅꜱ ᴘʀᴇꜰɪxᴇꜱ : `.` `/` `?` `!` -\nᴜꜱᴇʀ,ɪɴᴠɪᴛᴇ - ᴛᴏ ʀᴀɴᴅᴏᴍ ᴛᴀɢꜱ ᴛᴏ ᴜꜱᴇʀꜱ\n\nᴄᴀɴᴄʟᴇ,ꜱᴛᴏᴘᴀʟʟ,ᴏꜰꜰ - ᴛᴏ ᴛᴀɢᴀʟʟ ꜱᴛᴏᴘ\n\nᴇxᴀᴍᴘʟᴇꜱ : `user hii` \nꜰᴏʀ ꜱᴛᴏᴘ ᴛᴀɢꜱ ᴜꜱᴇ : `off`\n\nᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ :\n➻ `bots` : ʟɪꜱᴛ ᴀʟʟ ʙᴏᴛꜱ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ\n➻ `tgm` : ᴘɪᴄ 🇹ᴇʟᴇɢʀᴀᴘʜ ᴛᴏ ʟɪɴᴋ.\n➻ `stats` : ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘ ᴛᴏ ᴛɪᴍᴇ.\n➻ `tr` : ʏᴏᴜ ᴄᴀɴ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ɪɴ ᴀ ꜱɪᴍᴘʟᴇ ᴡᴀʏ.\n➻ `admins` : ɢᴇᴛ ᴀʟʟ ɢʀᴏᴜᴘꜱ ᴀᴅᴍɪɴ ʟɪꜱᴛꜱ.\n➻ `bots` : ɢᴇᴛ ᴀʟʟ ɢʀᴏᴜᴘꜱ ʙᴏᴛꜱ ʟɪꜱᴛꜱ.\n➻ `info`,`me`,`id` : ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴꜰᴏ ᴀɴᴅ ᴜꜱᴇʀꜱ ɪᴅ.\n➻ `repo` : ɢᴇᴛ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n➻ `bot` : ʜᴇʜᴇ.\n➻ `math ` : ᴍᴀᴛʜᴇᴍᴀᴛɪᴄꜱ.\n➻ ɢᴀᴍᴇꜱ : `dice` , `basket` , `jackpot` , `ball` , `football` \n➻ `AMBOT`,`am`,`@AM_YTBOTT` : ᴀᴍʙᴏᴛ ᴛᴀɢꜱ..\n➻ `Time` : ᴄᴜʀʀᴇɴᴛ ᴛɪᴍᴇ ɪɴ ɪɴᴅɪᴀ ..\n➻ `restart`,`reboot`,`reload` : ʀᴇꜱᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ꜰɪx ꜰᴏʀ ꜱʟᴏᴡ ᴄʜᴀᴛ..\n\n💕 ᴛʜɪꜱ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ : @AMBOTYT..\n\n🩷 ᴍᴏʀᴇ ꜰᴜɴᴄᴛɪᴏɴꜱ ᴀʀᴇ ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ...🩷 
"""
Ca = [
    "Matt Karo Na",
    "Me to BorHorahi hu",
    "Areee 😣",
    "Pls Yrr 😏",
    "Ab To Pitoge 🤧",
    "U Bad 💔",
    "😳",
]
SPAM_CHATS = []
TAGMES = [ " Hey Baby Kaha Ho 🥱🥺",
           " Oye So Gye Kya Online Aao Na 😊",
           " Vc Chalo Bate Karte Hain Kuch Kuch 😃 ",
           " Khana Kha Liya Ji ..??🥲 ",
           " Ghar MeSab Kaise Hai Ji 🥺",
           " Aapko Pata He Me Aapko Bahut Miss Karrahi Thi 🤭🙈",
           " Oye HaalChal Kaise He..??🤨 ",
           " Mere Se Setting Karoge ..??🙂 ",
           " Aapka Nama Kya he ..??🥲 ",
           " Naasta Huw Aapka ..??😋",
           " Mere Ko Apne Group Me Kidnap Karlo Na 😍 ",
           "𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅 ",
           "Mere Se Dosti Karoge..??🤔 ",
           " Sone Chale Gaya Kya 🙄🙄 ",
           " Aap Kaha Se Ho..??🙃 ",
           " Hello Ji Namaste 😛 ",
           " Hello Kkrh ..?🤔",
           " Do You Know Who Is My Owner.?😜😜 ",
           " Aur Batao Kaise Ho 😇 ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " Mere Se Baat Noi Katoge 🥺🥺",
           " Oye Pagal Online Aa ja 😶 ",
           " Oye Good Morning  😜",
           " Suno Ek Kaam Hai Tumse 🙂 ",
           " Nice To Meet Uh ☺ ",
           " Hello 🙊 ",
           " Bolo Na Kuch Yrr 🥲 ",
           " Tiger Queen Kon Hai...??😅 ",
           " Tumari Ek Pic Milgai ..?😅",
           " Mummy Aa Gyi Kya 😆😆😆",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " Do You Love Me ..?👀🙉",
           " Ek Song Sunau Na Pls ..😻😻 ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " Sara Kaam Khatam Hogaya Kya aapka ..?🙃",
           " Kaha Se Ho Aap 😊 ",
           " Sunno Na 🧐🧐 ",
           " Mera Ek Kaam Kardo Ge..?** ",
           " Kya Huw ..?👱 ",
           "Bahut Yaad Aarahe ho  🤧❣️ ",
           " U Bhul gaya Mujte 😏😏",
           " Jut Nahi Bolna Chaya Yrr  🤐 ",
           "Kha Lo Bhaw Matt Karo Baat 😒😒 ",
           " Hii 👀",
           " Aaj Mai Sad Hu ☹️ ",
           " Mujse V Cat Karlo Na 🥺🥺",
           " Kya Karr Rahe Ho 👀",
           " Kya Hal Chaal Hai 🙂",
           " Kaha Se Ho Aap..?🤔** ",
           " Chatt Karlo Na Group Me Mujse..🥺🥺",
           " Me Masoom Hu Thoda Sa 🥺🥺",
           " Kal Maja Aaya Tha Na 🤭😅 ",
          """Ek Jokes For U 🤭🤭
beta - pita ji, aap bahut kismat vaale hain? 
pita jee - vo kaise beta? 
beta - kyonki main fail ho gaya hoon, 
aapako mere liye nai kitaaben nahin kharidani padengi.""",
          """EK Song AapKe Liya 🥺🥺
Ye jo halka halka suroor hai
Ye teri nazar ka kusoor hai
Ke sharaab peena sikha diya
Tere pyaar ne teri chaah ne
Teri behki behki nigaah ne
Mujhe ek sharaabi bana diya
k sharab peena sikha diya""",
          "Me Telegram Delete Karne Wali Hu 🥺", 
          "Aapka Pata He Kya Group Ka Owner kON hE",
          "oii Date Pe Chalega Mere Sath..?🤭🙉",
          "U Gannda Bachha Online Nahi Aate 🤭",
          "Mera break up Hogaya Aaj 💔😣",
          "Thoda Meri tarif Kardo Na 🤭🙉",
          "Me AapKo Janti HuNa 😳",
          "Me Dekhrahi hu 👀👀",
          "Tumara V break up Hogaya He Kya ",
          "AapKo Achha Nahi Laga Vc Pe 🥺",
          "Suggest Kardo Na Group Me Kese Baad Karu ",
          "Chiiii 🤧",
          "[AMBOT Kon He Jaante Ho Kya 🤧](t.me/AM_YTBOTT)",
          "AajKal Tum Bahut Ignore Karte Ho HamKo 🤔",
          "Thoda Der Pehle Tumse Pyar Huw Ussi Time break up V Hogaya 🤭🤭",
          "Dekho Kese Kese Log He Ider 🤭",
          "Kya Huw Aapko 🥺🥺",
          "Muje AapSe Baat Nahi Karni 🥺",
          "Aapko Pata He Mere pass 10+ Dil He Ek Aapka V He 🤭",
          "Me JarahiHu 💔😣",
          "chalo Chalte He 🤭 ",
          "U 💔💔💔💔💔💔",
          
          
           ]
def get_current_time():
    tz = pytz.timezone('Asia/Kolkata')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z") 
@client.on_message(
    filters.command(["Time","time","Date","Date"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"ᴄᴜʀʀᴇɴᴛ ᴛɪᴍᴇ ɪɴ ɪɴᴅɪᴀ :\n {time}")
    
@client.on_message(
    filters.command(["restart","reboot","reload"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def restart_(_, message):
    response = await message.reply_text("ʀᴇsᴛᴀʀᴛɪɴɢ...")
    try:
        shutil.rmtree("downloads")
        shutil.rmtree("raw_files")
        shutil.rmtree("cache")
    except:
        pass
    await response.edit_text(
        "» ʀᴇsᴛᴀʀᴛ ᴘʀᴏᴄᴇss sᴛᴀʀᴛᴇᴅ, ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ ғᴏʀ ғᴇᴡ sᴇᴄᴏɴᴅs ᴜɴᴛɪʟ ᴛʜᴇ ʙᴏᴛ sᴛᴀʀᴛs..."
    )
    os.system(f"kill -9 {os.getpid()} && python3 main.py")
@client.on_message(
    filters.command(["dart","Dart"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def dart(client, message):
    x=await client.send_dice(message.chat.id, "🎯")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)

@client.on_message(
    filters.command(["basket","Basket"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def basket(client, message):
    x = await client.send_dice(message.chat.id, "🏀")
    m = x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}", quote=True)

@client.on_message(
    filters.command(["jackpot","Jackpot"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def jackpot(client, message):
    x = await client.send_dice(message.chat.id, "🎰")
    m = x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}", quote=True)

@client.on_message(
    filters.command(["ball","Ball"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def ball(client, message):
    x = await client.send_dice(message.chat.id, "🎳")
    m = x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}", quote=True)

@client.on_message(
    filters.command(["football","Football","FootBall"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def football(client, message):
    x = await client.send_dice(message.chat.id, "⚽")
    m = x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}", quote=True)

    
@client.on_message(
    filters.command(["math","Math"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
def calculate_math(client, message):   
    expression = message.text.split("math ", 1)[1]
    try:        
        result = eval(expression)
        response = f"ᴛʜᴇ ʀᴇsᴜʟᴛ ɪs : {result}"
    except:
        response = "ɪɴᴠᴀʟɪᴅ ᴇxᴘʀᴇssɪᴏɴ"
    message.reply(response)
# vc on
@client.on_message(filters.voice_chat_started)
async def brah(_, msg):
       await msg.reply("ᴠᴏɪᴄᴇ ᴄʜᴀᴛ sᴛᴀʀᴛᴇᴅ")
# vc off
@client.on_message(filters.voice_chat_ended)
async def brah2(_, msg):
       await msg.reply("**ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴇɴᴅᴇᴅ**")

# invite members on vc
@client.on_message(filters.voice_chat_members_invited)
async def brah3(client :client, message:Message):
           text = f"{message.from_user.mention} ɪɴᴠɪᴛᴇᴅ "
           x = 0
           for user in message.voice_chat_members_invited.users:
             try:
               text += f"[{user.first_name}](tg://user?id={user.id}) "
               x += 1
             except Exception:
               pass
           try:
             await message.reply(f"{text} 😉")
           except:
             pass
               
button_data = {}
mongo = MongoClient(MONGO_URL)
db = mongo.DAXXMUSIC
coupledb = db.couple
afkdb = db.afk
nightmodedb = db.nightmode
notesdb = db.notes
filtersdb = db.filters

#TGM 
@client.on_message(
    filters.command(["tgm","link"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
def ul(_, message):
    reply = message.reply_to_message
    if reply.media:
        i = message.reply("ᴘʟꜱ ᴡᴀɪᴛ ᴀ ᴍɪɴ...")
        path = reply.download()
        fk = upload_file(path)
        for x in fk:
            url = "https://telegra.ph" + x

        i.edit(f' 🇾ᴏᴜʀ🇹ᴇʟᴇɢʀᴀᴘʜ `{url}`')
        

@client.on_message(
    filters.command(["start"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def start(_, message):
    await message.reply_text(
        text=f"ʜᴇʟʟᴏ {message.from_user.mention}!\n ɪ ᴀᴍ ᴀ ᴄʜᴀᴛ + ᴛᴀɢ ᴀʟʟ ʙᴏᴛ, ᴄʀᴇᴀᴛᴇᴅ ʙʏ [ᴀᴍʙᴏᴛ](https://t.me/AM_YTBOTT).\n\nUse `help` ᴛᴏ ꜱᴇᴇ ᴛʜᴇ ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅꜱ.",
        disable_web_page_preview=True
    )
    
#Bot Stats
start_time = time.time()

def time_formatter(milliseconds):
    minutes, seconds = divmod(int(milliseconds / 1000), 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    weeks, days = divmod(days, 7)
    tmp = (((str(weeks) + "ᴡ:") if weeks else "") +
           ((str(days) + "ᴅ:") if days else "") +
           ((str(hours) + "ʜ:") if hours else "") +
           ((str(minutes) + "ᴍ:") if minutes else "") +
           ((str(seconds) + "s") if seconds else ""))
    if not tmp:
        return "0s"
    if tmp.endswith(":"):
        return tmp[:-1]
    return tmp
    
@client.on_message(
    filters.command(["stats"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def activevc(_, message: Message):
    uptime = time_formatter((time.time() - start_time) * 1000)
    cpu = psutil.cpu_percent()
    TEXT = f"**ᴜᴘᴛɪᴍᴇ** : {uptime} | **ᴄᴘᴜ** : {cpu}%"
    await message.reply(TEXT)
#Tr
trans = Translator()

@client.on_message(
    filters.command(["tr","Translator","Translat","Trt"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def translate(_, message) -> None:
    reply_msg = message.reply_to_message
    if not reply_msg:
        await message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ɪᴛ !")
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = await trans.detect(to_translate)
            dest = args
    except IndexError:
        source = await trans.detect(to_translate)
        dest = "en"
    translation = await trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} to {dest}:\n"
        f"{translation.text}"
    )
    await message.reply_text(reply)

#TagOff     
@client.on_message(
    filters.command(["cancel", "stopall", "off"], prefixes=["/", ".", "?", "-", "", "!"])
    & filters.group
)
async def cancelcmd(_, message):
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ["administrator", "creator"]:
        return await message.reply_text("**Only admins can use this command!**")

    if chat_id in SPAM_CHATS:
        try:
            SPAM_CHATS.remove(chat_id)
        except Exception:
            pass
            off = random.choice(Ca)
        return await message.reply_text(off)
    else:
        await message.reply_text("**No ongoing process!**")
        return

#Bots
@client.on_message(
    filters.command(["bots"], prefixes=["/", ".", "?", "-", "", "!"])
    & filters.group
)
async def list_bots(_, message):
    chat_id = message.chat.id
    chat_members = await client.get_chat_members(chat_id)
    bot_list = [member.user.username for member in chat_members if member.user and member.user.is_bot]
    
    if bot_list:
        bot_list_text = "\n├ @".join(bot_list)
        await message.reply_text(f"ʙᴏᴛ ʟɪsᴛ - {message.chat.title}**\n\n🤖 ʙᴏᴛs\n\n├ @{bot_list_text}")
    else:
        await message.reply_text("ᴛʜᴇʀᴇ ᴀʀᴇ ɴᴏ ʙᴏᴛꜱ ɪɴ ᴛʜɪꜱ ɢʀᴏᴜᴘ.")

#My Id 
@client.on_message(
    filters.command(["info","id"], prefixes=["/", ".", "?", "-", "", "!"])
    & filters.group
)
def group_status(client, message):
    chat = message.chat 
    chat_id = message.chat.id
    chat_info = client.get_chat(chat_id)
    title = chat_info.title
    description = chat_info.description
    member_count = chat_info.members_count
    reply = message.reply_to_message
    status_text = f"ᴄʜᴀᴛ ɪᴅ : `{chat.id}`\nᴄʜᴀᴛ ɴᴀᴍᴇ : `{title}`\nᴛʏᴘᴇ : `{chat.type}`\nᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : `{description}`\nᴍᴇᴍʙᴇʀꜱ ᴄᴏᴜɴᴛ : `{member_count}`\nʏᴏᴜʀ ɪᴅ: `{message.from_user.id}`\n"         
    if reply:
        message.reply_text(
            f"ᴄʜᴀᴛ ɪᴅ : `{chat.id}`\nᴄʜᴀᴛ ɴᴀᴍᴇ : `{title}`\nᴛʏᴘᴇ : `{chat.type}`\nᴅᴇꜱᴄʀɪᴘᴛɪᴏɴ : `{description}`\nᴍᴇᴍʙᴇʀꜱ ᴄᴏᴜɴᴛ : `{member_count}`\nʏᴏᴜʀ ɪᴅ : `{message.from_user.id}`\n{reply.from_user.first_name}'s ɪᴅ: `{reply.from_user.id}`\nʏᴏᴜʀ ɪᴅ: `{message.from_user.id}`\n"
        )
                  
    if chat.username:  # Not all groups have a username
        status_text += f"ᴜꜱᴇʀɴᴀᴍᴇ : @{chat.username}"
    else:
        status_text += "ᴜꜱᴇʀɴᴀᴍᴇ : `ɴᴏɴᴇ`"

    message.reply_text(status_text)


#help
@client.on_message(
    filters.command(["help"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def help_command(_, message):
    button_text = "ɢʙᴀɴꜱ ʟᴏɢꜱ"
    button_url = "https://t.me/Logs_Gban"
    button = InlineKeyboardButton(button_text, url=button_url)
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[button]])
    await message.reply_text(HELP, reply_markup=keyboard)

  #Repo  
@client.on_message(
    filters.command(["repo","source","code"], prefixes=["/", ".", "?", "-", "", "!",""])
    & ~filters.private
)
async def help_command(_, message):
    await message.reply_text(REPO)

#Bot
@client.on_message(
    filters.command(["bot"], prefixes=["/", ".", "?", "-", "", "!",""])
    & ~filters.private
)
async def help_command(_, message):
    text = random.choice(AAA)
    await message.reply_text(text)
#Tagall
@client.on_message(
    filters.command(["user", "invite"], prefixes=["/", ".", "?", "-", "", "!"])
    & filters.group
)
async def tag_all_users(_, message):
    chat_id = message.chat.id
    chat_member = await client.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status not in ["administrator", "creator"]:
        return await message.reply_text("**Only admins can use this command!**")
    replied = message.reply_to_message
    if len(message.command) < 2 and not replied:
        await message.reply_text("**Reply to a message or give some text to tag all!**")
        return
    text = random.choice(TAGMES)
    SPAM_CHATS.append(message.chat.id)
    usernum = 0
    usertxt = ""
    members = await client.get_chat_members(message.chat.id)
    member_iter = iter(members)
    while message.chat.id in SPAM_CHATS:
        try:
            m = next(member_iter)
            usernum += 1
            usertxt += f" [{m.user.first_name}](tg://user?id={m.user.id})\n"
            if usernum == 1:
                if replied:
                    await replied.reply_text(usertxt)
                else:
                    await client.send_message(message.chat.id, f'{random.choice(TAGMES)}\n{usertxt}')
                await asyncio.sleep(15)
                usernum = 0
                usertxt = ""
        except StopIteration:
            break

    try:
        SPAM_CHATS.remove(message.chat.id)
    except Exception:
        pass

@client.on_chat_member_updated()
async def welcome_message(_, update):
    new_chat_member = update.new_chat_member
    if new_chat_member and new_chat_member.status == "member":
        welcome_text = f"Welcome {new_chat_member.mention} to the group! 🎉"
        await client.send_message(update.chat.id, welcome_text)


#AM
@client.on_message(
    filters.command(["AM_YTBOTT","@AM_YTBOTT","@am_ytbott","ambot","am"], prefixes=["/", ".", "?", "-",""])
    & ~filters.private)
async def start(client, message):
    random_message = random.choice(AMTAGS)
    await message.reply_text(random_message)
    
@client.on_message(
    filters.text
    | filters.sticker
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})
       if not is_Daxx:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})      
           if k:               
               for x in is_chat:
                   K.append(x['text'])          
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "sticker":
                   await message.reply_sticker(f"{hey}")
               if not Yo == "sticker":
                   await message.reply_text(f"{hey}")
   
   if message.reply_to_message:  
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_Daxx:                   
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:       
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "sticker":
                       await message.reply_sticker(f"{hey}")
                   if not Yo == "sticker":
                       await message.reply_text(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})
       if not is_Daxx:
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       Daxxdb = MongoClient(MONGO_URL)
       Daxx = Daxxdb["DaxxDb"]["Daxx"] 
       is_Daxx = Daxx.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_Daxx:                    
               await client.send_chat_action(message.chat.id, "typing")
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   toggle.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    
              


@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxprivate(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]
   if not message.reply_to_message: 
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.text})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "sticker":
           await message.reply_sticker(f"{hey}")
       if not Yo == "sticker":
           await message.reply_text(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.text})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "sticker":
               await message.reply_sticker(f"{hey}")
           if not Yo == "sticker":
               await message.reply_text(f"{hey}")
                     
@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def Daxxprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, "typing")
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, "typing")
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
client.run()
