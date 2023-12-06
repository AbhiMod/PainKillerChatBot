from pyrogram import filters
from pyrogram.types import Message
from pyrogram import Client, filters
from pyrogram import enums, filters
from pyrogram.types import ChatMember
import asyncio
import psutil
from pyrogram.types import *
from pymongo import MongoClient
import requests
import os, time
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
from pyrogram.handlers import MessageHandler
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import HighQualityAudio, MediumQualityVideo
from pytgcalls.types.stream import StreamAudioEnded

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
sudos = 6204761408
REPO = """ᴍɪᴋᴀsʜᴀᴀ ᴀɪ⌫
<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎ ᴀᴍʙᴏᴛ:</u>

𝗥𝗘𝗣𝗢 ❥︎ [𝗥𝗘𝗣𝗢](t.me/About_AMBot)

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ [ɢʙᴀɴꜱ ʟᴏɢꜱ](https://t.me/Logs_Gban)

𝗢𝗪𝗡𝗘𝗥 ❥︎ [ᴀᴍʙᴏᴛ](https://t.me/AM_YTBOTT)"""
HELP = """ʜᴇʀᴇ ɪꜱ ᴄᴍᴅꜱ ꜰᴏʀ ᴛᴀɢᴀʟʟ\nᴜꜱᴇ ᴄᴍᴅꜱ ᴘʀᴇꜰɪxᴇꜱ : `.` `/` `?` `!` -\nᴜꜱᴇʀ,ɪɴᴠɪᴛᴇ - ᴛᴏ ʀᴀɴᴅᴏᴍ ᴛᴀɢꜱ ᴛᴏ ᴜꜱᴇʀꜱ\n\nᴄᴀɴᴄʟᴇ,ꜱᴛᴏᴘᴀʟʟ,ᴏꜰꜰ - ᴛᴏ ᴛᴀɢᴀʟʟ ꜱᴛᴏᴘ\n\nᴇxᴀᴍᴘʟᴇꜱ : `user hii` \nꜰᴏʀ ꜱᴛᴏᴘ ᴛᴀɢꜱ ᴜꜱᴇ : `off`\n\nᴀᴅᴅɪᴛɪᴏɴᴀʟ ᴄᴏᴍᴍᴀɴᴅꜱ :\n➻ `bots` : ʟɪꜱᴛ ᴀʟʟ ʙᴏᴛꜱ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ\n➻ `tgm` : ᴘɪᴄ 🇹ᴇʟᴇɢʀᴀᴘʜ ᴛᴏ ʟɪɴᴋ.\n➻ `afk ʀᴇᴀꜱᴏɴ` : ᴍᴀʀᴋ ʏᴏᴜʀꜱᴇʟꜰ ᴀꜱ ᴀꜰᴋ ᴀᴡᴀʏ ꜰʀᴏᴍ ᴋᴇʏʙᴏᴀʀᴅ.\n➻ `brb ʀᴇᴀꜱᴏɴ` : ꜱᴀᴍᴇ ᴀꜱ ᴛʜᴇ ᴀꜰᴋ ᴄᴏᴍᴍᴀɴᴅ - ʙᴜᴛ ɴᴏᴛ ᴀ ᴄᴏᴍᴍᴀɴᴅ.
ᴡʜᴇɴ ᴍᴀʀᴋᴇᴅ ᴀꜱ ᴀꜰᴋ, ᴀɴʏ ᴍᴇɴᴛɪᴏɴꜱ ᴡɪʟʟ ʙᴇ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴡɪᴛʜ ᴀ ᴍᴇꜱꜱᴀɢᴇ ᴛᴏ ꜱᴀʏ ʏᴏᴜ'ʀᴇ ɴᴏᴛ ᴀᴠᴀɪʟᴀʙʟᴇ!\n➻ `stats` : ᴄʜᴇᴄᴋ ʙᴏᴛ ᴜᴘ ᴛᴏ ᴛɪᴍᴇ.\n➻ `tr` : ʏᴏᴜ ᴄᴀɴ ᴛʀᴀɴꜱʟᴀᴛᴇ ᴍᴇꜱꜱᴀɢᴇꜱ ᴏɴ ᴛᴇʟᴇɢʀᴀᴍ ɪɴ ᴀ ꜱɪᴍᴘʟᴇ ᴡᴀʏ.\n➻ `admins` : ɢᴇᴛ ᴀʟʟ ɢʀᴏᴜᴘꜱ ᴀᴅᴍɪɴ ʟɪꜱᴛꜱ.\n➻ `bots` : ɢᴇᴛ ᴀʟʟ ɢʀᴏᴜᴘꜱ ʙᴏᴛꜱ ʟɪꜱᴛꜱ.\n➻ `info`,`me`,`id` : ɢᴇᴛ ɢʀᴏᴜᴘ ɪɴꜰᴏ ᴀɴᴅ ᴜꜱᴇʀꜱ ɪᴅ.\n➻ `repo` : ɢᴇᴛ ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ.\n➻ `bot` : ʜᴇʜᴇ.\n➻ `math ` : ᴍᴀᴛʜᴇᴍᴀᴛɪᴄꜱ.\n➻ ɢᴀᴍᴇꜱ : `dice` , `basket` , `jackpot` , `ball` , `football` \n➻ `AMBOT`,`am`,`@AM_YTBOTT` : ᴀᴍʙᴏᴛ ᴛᴀɢꜱ..\n\n💕 ᴛʜɪꜱ ʙᴏᴛ ᴍᴀᴅᴇ ʙʏ : @AMBOTYT..\n\n🩷 ᴍᴏʀᴇ ꜰᴜɴᴄᴛɪᴏɴꜱ ᴀʀᴇ ᴄᴏᴍɪɴɢ ꜱᴏᴏɴ...🩷 
"""
SPAM_CHATS = []
TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",
           " **𝐕𝐜 𝐂𝐡𝐚𝐥𝐨 𝐁𝐚𝐭𝐞𝐧 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧 𝐊𝐮𝐜𝐡 𝐊𝐮𝐜𝐡😃** ",
           " **𝐊𝐡𝐚𝐧𝐚 𝐊𝐡𝐚 𝐋𝐢𝐲𝐞 𝐉𝐢..??🥲** ",
           " **𝐆𝐡𝐚𝐫 𝐌𝐞 𝐒𝐚𝐛 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧 𝐉𝐢🥺** ",
           " **𝐏𝐭𝐚 𝐇𝐚𝐢 𝐁𝐨𝐡𝐨𝐭 𝐌𝐢𝐬𝐬 𝐊𝐚𝐫 𝐑𝐡𝐢 𝐓𝐡𝐢 𝐀𝐚𝐩𝐤𝐨🤭** ",
           " **𝐎𝐲𝐞 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐊𝐞𝐬𝐚 𝐇𝐚𝐢..??🤨** ",
           " **𝐌𝐞𝐫𝐢 𝐁𝐡𝐢 𝐒𝐞𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫𝐛𝐚 𝐃𝐨𝐠𝐞..??🙂** ",
           " **𝐀𝐚𝐩𝐤𝐚 𝐍𝐚𝐦𝐞 𝐊𝐲𝐚 𝐡𝐚𝐢..??🥲** ",
           " **𝐍𝐚𝐬𝐭𝐚 𝐇𝐮𝐚 𝐀𝐚𝐩𝐤𝐚..??😋** ",
           " **𝐌𝐞𝐫𝐞 𝐊𝐨 𝐀𝐩𝐧𝐞 𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐊𝐢𝐝𝐧𝐚𝐩 𝐊𝐫 𝐋𝐨😍** ",
           " **𝐀𝐚𝐩𝐤𝐢 𝐏𝐚𝐫𝐭𝐧𝐞𝐫 𝐀𝐚𝐩𝐤𝐨 𝐃𝐡𝐮𝐧𝐝 𝐑𝐡𝐞 𝐇𝐚𝐢𝐧 𝐉𝐥𝐝𝐢 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐲𝐢𝐚𝐞😅😅** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐃𝐨𝐬𝐭𝐢 𝐊𝐫𝐨𝐠𝐞..??🤔** ",
           " **𝐒𝐨𝐧𝐞 𝐂𝐡𝐚𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🙄🙄** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚 𝐏𝐥𝐬𝐬😕** ",
           " **𝐀𝐚𝐩 𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨..??🙃** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐉𝐢 𝐍𝐚𝐦𝐚𝐬𝐭𝐞😛** ",
           " **𝐇𝐞𝐥𝐥𝐨 𝐁𝐚𝐛𝐲 𝐊𝐤𝐫𝐡..?🤔** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐊𝐧𝐨𝐰 𝐖𝐡𝐨 𝐈𝐬 𝐌𝐲 𝐎𝐰𝐧𝐞𝐫.?** ",
           " **𝐂𝐡𝐥𝐨 𝐊𝐮𝐜𝐡 𝐆𝐚𝐦𝐞 𝐊𝐡𝐞𝐥𝐭𝐞 𝐇𝐚𝐢𝐧.🤗** ",
           " **𝐀𝐮𝐫 𝐁𝐚𝐭𝐚𝐨 𝐊𝐚𝐢𝐬𝐞 𝐇𝐨 𝐁𝐚𝐛𝐲😇** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐌𝐮𝐦𝐦𝐲 𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐢 𝐇𝐚𝐢🤭** ",
           " **𝐌𝐞𝐫𝐞 𝐒𝐞 𝐁𝐚𝐭 𝐍𝐨𝐢 𝐊𝐫𝐨𝐠𝐞🥺🥺** ",
           " **𝐎𝐲𝐞 𝐏𝐚𝐠𝐚𝐥 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚😶** ",
           " **𝐀𝐚𝐣 𝐇𝐨𝐥𝐢𝐝𝐚𝐲 𝐇𝐚𝐢 𝐊𝐲𝐚 𝐒𝐜𝐡𝐨𝐨𝐥 𝐌𝐞..??🤔** ",
           " **𝐎𝐲𝐞 𝐆𝐨𝐨𝐝 𝐌𝐨𝐫𝐧𝐢𝐧𝐠😜** ",
           " **𝐒𝐮𝐧𝐨 𝐄𝐤 𝐊𝐚𝐦 𝐇𝐚𝐢 𝐓𝐮𝐦𝐬𝐞🙂** ",
           " **𝐊𝐨𝐢 𝐒𝐨𝐧𝐠 𝐏𝐥𝐚𝐲 𝐊𝐫𝐨 𝐍𝐚😪** ",
           " **𝐍𝐢𝐜𝐞 𝐓𝐨 𝐌𝐞𝐞𝐭 𝐔𝐡☺** ",
           " **𝐇𝐞𝐥𝐥𝐨🙊** ",
           " **𝐒𝐭𝐮𝐝𝐲 𝐂𝐨𝐦𝐥𝐞𝐭𝐞 𝐇𝐮𝐚??😺** ",
           " **𝐁𝐨𝐥𝐨 𝐍𝐚 𝐊𝐮𝐜𝐡 𝐘𝐫𝐫🥲** ",
           " **𝐒𝐨𝐧𝐚𝐥𝐢 𝐊𝐨𝐧 𝐇𝐚𝐢...??😅** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐢 𝐄𝐤 𝐏𝐢𝐜 𝐌𝐢𝐥𝐞𝐠𝐢..?😅** ",
           " **𝐌𝐮𝐦𝐦𝐲 𝐀𝐚 𝐆𝐲𝐢 𝐊𝐲𝐚😆😆😆** ",
           " **𝐎𝐫 𝐁𝐚𝐭𝐚𝐨 𝐁𝐡𝐚𝐛𝐡𝐢 𝐊𝐚𝐢𝐬𝐢 𝐇𝐚𝐢😉** ",
           " **𝐃𝐨 𝐘𝐨𝐮 𝐋𝐨𝐯𝐞 𝐌𝐞..?👀** ",
           " **𝐑𝐚𝐤𝐡𝐢 𝐊𝐚𝐛 𝐁𝐚𝐧𝐝 𝐑𝐚𝐡𝐢 𝐇𝐨.??🙉** ",
           " **𝐄𝐤 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚𝐮..?😹** ",
           " **𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚 𝐉𝐚 𝐑𝐞 𝐒𝐨𝐧𝐠 𝐒𝐮𝐧𝐚 𝐑𝐚𝐡𝐢 𝐇𝐮😻** ",
           " **𝐈𝐧𝐬𝐭𝐚𝐠𝐫𝐚𝐦 𝐂𝐡𝐚𝐥𝐚𝐭𝐞 𝐇𝐨..??🙃** ",
           " **𝐖𝐡𝐚𝐭𝐬𝐚𝐩𝐩 𝐍𝐮𝐦𝐛𝐞𝐫 𝐃𝐨𝐠𝐞 𝐀𝐩𝐧𝐚 𝐓𝐮𝐦..?😕** ",
           " **𝐓𝐮𝐦𝐡𝐞 𝐊𝐨𝐧 𝐒𝐚 𝐌𝐮𝐬𝐢𝐜 𝐒𝐮𝐧𝐧𝐚 𝐏𝐚𝐬𝐚𝐧𝐝 𝐇𝐚𝐢..?🙃** ",
           " **𝐒𝐚𝐫𝐚 𝐊𝐚𝐦 𝐊𝐡𝐚𝐭𝐚𝐦 𝐇𝐨 𝐆𝐲𝐚 𝐀𝐚𝐩𝐤𝐚..?🙃** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩😊** ",
           " **𝐒𝐮𝐧𝐨 𝐍𝐚🧐** ",
           " **𝐌𝐞𝐫𝐚 𝐄𝐤 𝐊𝐚𝐚𝐦 𝐊𝐚𝐫 𝐃𝐨𝐠𝐞..?** ",
           " **𝐁𝐲 𝐓𝐚𝐭𝐚 𝐌𝐚𝐭 𝐁𝐚𝐭 𝐊𝐚𝐫𝐧𝐚 𝐀𝐚𝐣 𝐊𝐞 𝐁𝐚𝐝😠** ",
           " **𝐌𝐨𝐦 𝐃𝐚𝐝 𝐊𝐚𝐢𝐬𝐞 𝐇𝐚𝐢𝐧..?❤** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚..?👱** ",
           " **𝐁𝐨𝐡𝐨𝐭 𝐘𝐚𝐚𝐝 𝐀𝐚 𝐑𝐡𝐢 𝐇𝐚𝐢 🤧❣️** ",
           " **𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐌𝐮𝐣𝐡𝐞😏😏** ",
           " **𝐉𝐮𝐭𝐡 𝐍𝐡𝐢 𝐁𝐨𝐥𝐧𝐚 𝐂𝐡𝐚𝐡𝐢𝐲𝐞🤐** ",
           " **𝐊𝐡𝐚 𝐋𝐨 𝐁𝐡𝐚𝐰 𝐌𝐚𝐭 𝐊𝐫𝐨 𝐁𝐚𝐚𝐭😒** ",
           " **𝐊𝐲𝐚 𝐇𝐮𝐚😮😮** "
           " **𝐇𝐢𝐢👀** ",
           " **𝐀𝐚𝐩𝐤𝐞 𝐉𝐚𝐢𝐬𝐚 𝐃𝐨𝐬𝐭 𝐇𝐨 𝐒𝐚𝐭𝐡 𝐌𝐞 𝐅𝐢𝐫 𝐆𝐮𝐦 𝐊𝐢𝐬 𝐁𝐚𝐭 𝐊𝐚 🙈** ",
           " **𝐀𝐚𝐣 𝐌𝐚𝐢 𝐒𝐚𝐝 𝐇𝐮 ☹️** ",
           " **𝐌𝐮𝐬𝐣𝐡𝐬𝐞 𝐁𝐡𝐢 𝐁𝐚𝐭 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚 🥺🥺** ",
           " **𝐊𝐲𝐚 𝐊𝐚𝐫 𝐑𝐚𝐡𝐞 𝐇𝐨👀** ",
           " **𝐊𝐲𝐚 𝐇𝐚𝐥 𝐂𝐡𝐚𝐥 𝐇𝐚𝐢 🙂** ",
           " **𝐊𝐚𝐡𝐚 𝐒𝐞 𝐇𝐨 𝐀𝐚𝐩..?🤔** ",
           " **𝐂𝐡𝐚𝐭𝐭𝐢𝐧𝐠 𝐊𝐚𝐫 𝐋𝐨 𝐍𝐚..🥺** ",
           " **𝐌𝐞 𝐌𝐚𝐬𝐨𝐨𝐦 𝐇𝐮 𝐍𝐚🥺🥺** ",
           " **𝐊𝐚𝐥 𝐌𝐚𝐣𝐚 𝐀𝐲𝐚 𝐓𝐡𝐚 𝐍𝐚🤭😅** ",
           " **𝐆𝐫𝐨𝐮𝐩 𝐌𝐞 𝐁𝐚𝐭 𝐊𝐲𝐮 𝐍𝐚𝐡𝐢 𝐊𝐚𝐫𝐭𝐞 𝐇𝐨😕** ",
           " **𝐀𝐚𝐩 𝐑𝐞𝐥𝐚𝐭𝐢𝐨𝐦𝐬𝐡𝐢𝐩 𝐌𝐞 𝐇𝐨..?👀** ",
           " **𝐊𝐢𝐭𝐧𝐚 𝐂𝐡𝐮𝐩 𝐑𝐚𝐡𝐭𝐞 𝐇𝐨 𝐘𝐫𝐫😼** ",
           " **𝐀𝐚𝐩𝐤𝐨 𝐆𝐚𝐧𝐚 𝐆𝐚𝐧𝐞 𝐀𝐚𝐭𝐚 𝐇𝐚𝐢..?😸** ",
           " **𝐆𝐡𝐮𝐦𝐧𝐞 𝐂𝐡𝐚𝐥𝐨𝐠𝐞..??🙈** ",
           " **𝐊𝐡𝐮𝐬 𝐑𝐚𝐡𝐚 𝐊𝐚𝐫𝐨 ✌️🤞** ",
           " **𝐇𝐚𝐦 𝐃𝐨𝐬𝐭 𝐁𝐚𝐧 𝐒𝐚𝐤𝐭𝐞 𝐇𝐚𝐢...?🥰** ",
           " **𝐊𝐮𝐜𝐡 𝐁𝐨𝐥 𝐊𝐲𝐮 𝐍𝐡𝐢 𝐑𝐚𝐡𝐞 𝐇𝐨..🥺🥺** ",
           " **𝐊𝐮𝐜𝐡 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 𝐀𝐝𝐝 𝐊𝐚𝐫 𝐃𝐨 🥲** ",
           " **𝐒𝐢𝐧𝐠𝐥𝐞 𝐇𝐨 𝐘𝐚 𝐌𝐢𝐧𝐠𝐥𝐞 😉** ",
           " **𝐀𝐚𝐨 𝐏𝐚𝐫𝐭𝐲 𝐊𝐚𝐫𝐭𝐞 𝐇𝐚𝐢𝐧😋🥳** ",
           " **𝐇𝐞𝐦𝐥𝐨𝐨🧐** ",
           " **𝐌𝐮𝐣𝐡𝐞 𝐁𝐡𝐮𝐥 𝐆𝐲𝐞 𝐊𝐲𝐚🥺** ",
           " **𝐓𝐫𝐮𝐭𝐡 𝐀𝐧𝐝 𝐃𝐚𝐫𝐞 𝐊𝐡𝐞𝐥𝐨𝐠𝐞..? 😊** ",
           " **𝐀𝐚𝐣 𝐌𝐮𝐦𝐦𝐲 𝐍𝐞 𝐃𝐚𝐭𝐚 𝐘𝐫🥺🥺** ",
           " **𝐄𝐤 𝐃𝐢𝐥 𝐇𝐚𝐢 𝐄𝐤 𝐃𝐢𝐥 𝐇𝐢 𝐓𝐨 𝐇𝐚𝐢😗😗** ",
           " **𝐓𝐮𝐦𝐡𝐚𝐫𝐞 𝐃𝐨𝐬𝐭 𝐊𝐚𝐡𝐚 𝐆𝐲𝐞🥺** ",
           " **𝐊𝐚𝐡𝐚 𝐊𝐡𝐨𝐲𝐞 𝐇𝐨 𝐉𝐚𝐚𝐧😜** ",
           " **𝐆𝐨𝐨𝐝 𝐍8 𝐉𝐢 𝐁𝐡𝐮𝐭 𝐑𝐚𝐭 𝐇𝐨 𝐠𝐲𝐢🥰** ",
          " **𝐎𝐢𝐢 𝐕𝐜 𝐚𝐚𝐣𝐚𝐨 𝐁𝐚𝐫𝐧𝐚𝐚 𝐌𝐞 𝐓𝐮𝐦𝐤𝐨** 🤭🤭",
          " **𝐀𝐚𝐩 𝐎𝐧𝐥𝐢𝐧𝐞 𝐐 𝐧𝐚𝐡𝐢 𝐀𝐚𝐭𝐚 𝐡𝐞**🥺🥺 ",
          " 𝐌𝐞 𝐀𝐚𝐩 𝐒𝐞 𝐁𝐚𝐡𝐮𝐭 𝐆𝐡𝐮𝐬𝐬𝐚 𝐇𝐮 😣🙁😡",
          " 𝐀𝐚𝐩𝐤𝐨 𝐩𝐚𝐭𝐚 𝐡𝐞 𝐤𝐲𝐚 🙊🙊",
          " 𝐔𝐥𝐥𝐞 😳😳",
          "𝐓𝐮𝐦𝐚𝐫𝐢 𝐅𝐫𝐢𝐞𝐧𝐝 𝐧𝐞 𝐭𝐲𝐦𝐤𝐨 𝐰𝐨 𝐝𝐢𝐲𝐚 𝐭𝐡𝐚 𝐧𝐚𝐚...😳😳",
          "𝐀𝐚𝐣𝐚 𝐓𝐨 𝐇𝐨𝐠𝐚 𝐩𝐚𝐫𝐭𝐲 𝐖𝐨 𝐯 𝐓𝐮𝐦𝐚𝐫𝐞 𝐓𝐚𝐫𝐟𝐬𝐞 😜😂😂",
          "𝐁𝐚𝐛𝐲 𝐁𝐚𝐧𝐚𝐥𝐨 𝐍𝐚 𝐦𝐮𝐣𝐞 🙈🙈",
          "𝐊𝐲𝐚 𝐀𝐚𝐩 𝐌𝐞𝐫𝐞 𝐒𝐞 𝐂𝐡𝐚𝐭 𝐊𝐚𝐫𝐨 𝐠𝐞 😋😋",
          " 𝐀𝐚𝐣 𝐭𝐨 𝐌𝐞𝐫𝐞 𝐘𝐚𝐚𝐫 𝐊𝐢 𝐏𝐚𝐫𝐭𝐲 𝐇𝐞 🤫🤭🤭",
          "𝐓𝐮𝐦𝐚𝐫𝐚 𝐈𝐝 𝐝𝐞𝐤𝐡𝐚 𝐭𝐨 𝐲𝐞𝐬𝐚 𝐥𝐚𝐠𝐚 𝐣𝐞𝐬𝐚 𝐄𝐤 𝐯 𝐓𝐚𝐠 𝐧𝐚 𝐤𝐚𝐫𝐮 😏😏",
          " 𝐀𝐚𝐩 𝐧𝐞 𝐧𝐚𝐚𝐦 𝐂𝐡𝐚𝐧𝐠𝐞 𝐤𝐢𝐲𝐚 𝐤𝐲𝐚 😝😝",
          " **𝐌𝐞𝐧𝐞 𝐃𝐞𝐤𝐡 𝐥𝐢𝐲𝐚 𝐬𝐚𝐛 👀🙈** ",
          " **𝐌𝐞𝐫𝐢 𝐄𝐤 𝐅𝐫𝐢𝐞𝐧𝐝 𝐡𝐞 𝐰𝐨 𝐛𝐚𝐡𝐮𝐭 𝐟𝐥𝐢𝐫𝐭 𝐤𝐚𝐫𝐭𝐢 𝐡𝐞** 🥺🥺 ",
          " 𝐇𝐨𝐰 𝐓𝐨 𝐌𝐚𝐤𝐞 𝐆𝐟 𝐒𝐢𝐤𝐤𝐧𝐚 𝐇𝐞 𝐤𝐲𝐚 𝐀𝐚𝐩𝐤𝐨 🤫🤫",
          " 𝐀𝐚𝐩 𝐧𝐞 𝐦𝐮𝐣𝐞 𝐛𝐥𝐨𝐜𝐤 𝐪 𝐤𝐢𝐲𝐚 𝐦𝐞𝐧𝐞 𝐭𝐨 𝐛𝐚𝐬𝐬 𝐢 𝐥𝐨𝐯𝐞 𝐮 𝐛𝐨𝐥𝐚 𝐭𝐡𝐚 🥺🥺",
          " 𝐌𝐮𝐣𝐞 𝐕 𝐀𝐝𝐦𝐢𝐧 𝐁𝐚𝐧𝐰𝐚 𝐝𝐨 𝐧𝐚 😔😔",
          " @AM_YTBOTT 𝐈𝐬𝐤𝐨 𝐒𝐚𝐦𝐣𝐚 𝐝𝐨 𝐌𝐮𝐣𝐞 𝐧𝐚 𝐜𝐡𝐞𝐝𝐞 😢😭",
          "𝐀𝐚𝐩𝐤𝐨 𝐆𝐟 𝐂𝐡𝐚𝐲𝐚 𝐊𝐲𝐚 𝐌𝐞 𝐒𝐞𝐥𝐥 𝐤𝐚𝐫𝐭𝐢 𝐇𝐮 𝟏𝟎𝐫𝐬 𝐤𝐚 𝐭𝐮𝐫𝐭𝐮𝐫𝐞 🤭🤭",
          " 𝐚𝐧𝐝𝐢 𝐦𝐚𝐧𝐝𝐢 𝐬𝐚𝐧𝐝𝐢 𝐯𝐜 𝐩𝐞 𝐧𝐚𝐡𝐢 𝐚𝐚𝐨 𝐠𝐞 𝐭𝐨 ... 😂😂",
          " 𝐞𝐤 𝐬𝐨𝐧𝐠 𝐟𝐨𝐫 𝐮 𝐎 𝐦𝐞𝐫𝐞 𝐬𝐚𝐧𝐚𝐦 𝐭𝐞𝐫𝐞 𝐡𝐚𝐦 𝐝𝐚𝐦 🤗🤗",
           ]


@client.on_message(~filters.private & filters.command(["gstatus","gstats"]), group=2)
async def instatus(client, message):
    start_time = time.perf_counter()
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    count = await client.get_chat_members_count(message.chat.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        sent_message = await message.reply_text("GETTING INFORMATION...")
        deleted_acc = 0
        premium_acc = 0
        banned = 0
        bot = 0
        uncached = 0
        async for ban in client.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.BANNED):
            banned += 1
        async for member in client.get_chat_members(message.chat.id):
            user = member.user
            if user.is_deleted:
                deleted_acc += 1
            elif user.is_bot:
                bot += 1
            elif user.is_premium:
                premium_acc += 1
            else:
                uncached += 1
        end_time = time.perf_counter()
        timelog = "{:.2f}".format(end_time - start_time)
        await sent_message.edit(f"""
**➖➖➖➖➖➖➖
➲ NAME : {message.chat.title} ✅
➲ MEMBERS : [ {count} ]🫂
➖➖➖➖➖➖➖
➲ BOTS : {bot}💡
➲ ZOMBIES : {deleted_acc}🧟
➲ BANNED : {banned}🚫
➲ PREMIUM USERS : {premium_acc}🎁
➖➖➖➖➖➖➖
TIME TAKEN : {timelog} S**""")
    else:
        sent_message = await message.reply_text("ONLY ADMINS CAN USE THIS !")
        await sleep(5)
        await sent_message.delete()
        
@client.on_message(
    filters.command(["dice","Dice"], prefixes=["/", ".", "?", "-", "", "!"])
    & ~filters.private
)
async def dice(client, message):
    x=await client.send_dice(message.chat.id,"🎲")
    m=x.dice.value
    await message.reply_text(f"Hey {message.from_user.mention} your Score is : {m}",quote=True)

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
        return await message.reply_text("**Ok Yrr Ab Yesa Lagraha me spam karr jesa ab nahi tag karraha me kisi ko!**")
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
