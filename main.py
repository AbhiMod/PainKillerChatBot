from pyrogram import filters
from pyrogram import Client, filters
from pyrogram.types import ChatMember
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re
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

REPO = """ᴍɪᴋᴀsʜᴀᴀ ᴀɪ⌫

<u>𝗖𝗥𝗘𝗗𝗜𝗧 ❥︎ ᴀᴍʙᴏᴛ:</u>

𝗥𝗘𝗣𝗢 ❥︎ [𝗥𝗘𝗣𝗢](t.me/About_AMBot)

𝗖𝗛𝗔𝗡𝗡𝗘𝗟 ❥︎ [ɢʙᴀɴꜱ ʟᴏɢꜱ](https://t.me/Logs_Gban)

𝗢𝗪𝗡𝗘𝗥 ❥︎ [ᴀᴍʙᴏᴛ](https://t.me/AM_YTBOTT)"""
HELP = "ʜᴇʀᴇ ɪꜱ ᴄᴍᴅꜱ ꜰᴏʀ ᴛᴀɢᴀʟʟ\nᴜꜱᴇ ᴄᴍᴅꜱ ᴘʀᴇꜰɪxᴇꜱ : `.` `/` `?` `!` -\nᴜꜱᴇʀ,ɪɴᴠɪᴛᴇ - ᴛᴏ ʀᴀɴᴅᴏᴍ ᴛᴀɢꜱ ᴛᴏ ᴜꜱᴇʀꜱ\n\nᴄᴀɴᴄʟᴇ,ꜱᴛᴏᴘᴀʟʟ,ᴏꜰꜰ - ᴛᴏ ᴛᴀɢᴀʟʟ ꜱᴛᴏᴘ\n\nᴇxᴀᴍᴘʟᴇꜱ : `user hii` \nꜰᴏʀ ꜱᴛᴏᴘ ᴛᴀɢꜱ ᴜꜱᴇ : `off`"
SPAM_CHATS = []
TAGMES = [ " **𝐇𝐞𝐲 𝐁𝐚𝐛𝐲 𝐊𝐚𝐡𝐚 𝐇𝐨🥱** ",
           " **𝐎𝐲𝐞 𝐒𝐨 𝐆𝐲𝐞 𝐊𝐲𝐚 𝐎𝐧𝐥𝐢𝐧𝐞 𝐀𝐚𝐨😊** ",

           ]

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
        return await message.reply_text("**Tag all successfully stopped!**")
    else:
        await message.reply_text("**No ongoing process!**")
        return


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

    
@client.on_message(
    filters.command(["repo","source","code"], prefixes=["/", ".", "?", "-", "", "!",""])
    & ~filters.private
)
async def help_command(_, message):
    await message.reply_text(REPO)


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
                await asyncio.sleep(10)
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
               

#Welcome
class WelDatabase:
    def __init__(self):
        self.data = {}

    async def find_one(self, chat_id):
        return chat_id in self.data

    async def add_wlcm(self, chat_id):
        self.data[chat_id] = {}  # You can store additional information related to the chat
        # For example, self.data[chat_id]['some_key'] = 'some_value'

    async def rm_wlcm(self, chat_id):
        if chat_id in self.data:
            del self.data[chat_id]

wlcm = WelDatabase()

class temp:
    ME = None
    CURRENT = 2
    CANCEL = False
    MELCOW = {}
    U_NAME = None
    B_NAME = None

def circle(pfp, size=(500, 500)):
    pfp = pfp.resize(size, Image.ANTIALIAS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.ANTIALIAS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

def welcomepic(pic, user, chat, id, uname):
    background = Image.open("assets/bg2.jpg")
    pfp = Image.open(pic).convert("RGBA")
    pfp = circle(pfp)
    pfp = pfp.resize((450, 450))
    draw = ImageDraw.Draw(background)
    font = ImageFont.truetype('assets/font.ttf', size=40)
    welcome_font = ImageFont.truetype('assets/font.ttf', size=60)
    draw.text((30, 300), f'NAME: {user}', fill=(255, 255, 255), font=font)
    draw.text((30, 370), f'ID: {id}', fill=(255, 255, 255), font=font)
    draw.text((30, 40), f"{chat}", fill=(225, 225, 225), font=welcome_font)
    draw.text((30, 430), f"USERNAME : {uname}", fill=(255, 255, 255), font=font)
    pfp_position = (671, 134)
    background.paste(pfp, pfp_position, pfp)
    background.save(f"downloads/welcome#{id}.png")
    return f"downloads/welcome#{id}.png"
    
@client.on_message(filters.command("wel") & ~filters.private)
async def auto_state(_, message):
    usage = "**Usage:**\n⦿/wel [on|off]\n➤sᴀʟᴏɴ ᴀᴜʀ ʜᴀᴀɴ sᴛʏʟɪsʜ ғᴏɴᴛ ɴᴏᴛ ᴀʟʟᴏᴡᴇᴅ ɪɴ ᴛʜᴇ ᴛʜᴜᴍʙɴᴀɪʟ.!"
    if len(message.command) == 1:
        return await message.reply_text(usage)
    chat_id = message.chat.id
    user = await client.get_chat_member(message.chat.id, message.from_user.id)
    if user.status in (
        enums.ChatMemberStatus.ADMINISTRATOR,
        enums.ChatMemberStatus.OWNER,
    ):
        A = await wlcm.find_one(chat_id)
        state = message.text.split(None, 1)[1].strip().lower()
        if state == "on":
            if A:
                return await message.reply_text("Special Welcome Already Enabled")
            elif not A:
                await wlcm.add_wlcm(chat_id)
                await message.reply_text(f"Enabled Special Welcome in {message.chat.title}")
        elif state == "off":
            if not A:
                return await message.reply_text("Special Welcome Already Disabled")
            elif A:
                await wlcm.rm_wlcm(chat_id)
                await message.reply_text(f"Disabled Special Welcome in {message.chat.title}")
        else:
            await message.reply_text(usage)
    else:
        await message.reply("Only Admins Can Use This Command")
@client.on_chat_member_updated(filters.group, group=-3)
async def greet_group(_, member: ChatMemberUpdated):
    chat_id = member.chat.id
    A = await wlcm.find_one(chat_id)  # Corrected this line
    if not A:
        return
    if (
        not member.new_chat_member
        or member.new_chat_member.status in {"banned", "left", "restricted"}
        or member.old_chat_member
    ):
        return
    user = member.new_chat_member.user if member.new_chat_member else member.from_user
    try:
        pic = await client.download_media(
            user.photo.big_file_id, file_name=f"pp{user.id}.png"
        )
    except AttributeError:
        pic = "assets/bg2.jpg"
    if (temp.MELCOW).get(f"welcome-{member.chat.id}") is not None:
        try:
            await temp.MELCOW[f"welcome-{member.chat.id}"].delete()
        except Exception as e:
            LOGGER.error(e)
    try:
        welcomeimg = welcomepic(
            pic, user.first_name, member.chat.title, user.id, user.username
        )
        temp.MELCOW[f"welcome-{member.chat.id}"] = await client.send_photo(
            member.chat.id,
            photo=welcomeimg,
            caption=f"""
**Wᴇʟᴄᴏᴍᴇ Tᴏ {member.chat.title}
➖➖➖➖➖➖➖➖➖➖➖➖
Nᴀᴍᴇ ✧ {user.mention}
Iᴅ ✧ {user.id}
Usᴇʀɴᴀᴍᴇ ✧ @{user.username}
➖➖➖➖➖➖➖➖➖➖➖➖**
""",
            reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"⦿ ᴀᴅᴅ ᴍᴇ ⦿", url=f"https://t.me/MikaShaaAIBot?startgroup=true")]])
        )
    except Exception as e:
        LOGGER.error(e)
    try:
        os.remove(f"downloads/welcome#{user.id}.png")
        os.remove(f"downloads/pp{user.id}.png")
    except Exception as e:
        pass
@client.on_message(filters.new_chat_members & filters.group, group=-1)
async def bot_wel(_, message):
    for u in message.new_chat_members:
        if u.id == (await client.get_me()).id:
            await client.send_message(LOG_CHANNEL_ID, f"""
**NEW GROUP
➖➖➖➖➖➖➖➖➖➖➖➖
NAME: {message.chat.title}
ID: {message.chat.id}
USERNAME: @{message.chat.username}
➖➖➖➖➖➖➖➖➖➖➖➖**
""")
client.run()
