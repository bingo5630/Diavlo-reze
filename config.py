#Recoded by @Its_Oreki_Hotarou

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8556620780:AAF7i3mlk4DIoaOvi6Y026B_biXkffy6NpI")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "26944587"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7261a455f2a6159b8a2fbfecd1a63004")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002556901732"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6888478102"))

#Port
PORT = os.environ.get("PORT", "5004")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://sanjisama626:sanjisama626@sanjisama.lukxw8r.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Reze_ribot")

#force sub channel id, if you want enable force sub
FORCESUB_CHANNEL = int(os.environ.get("FORCESUB_CHANNEL", "-1002584481539"))
FORCESUB_CHANNEL2 = int(os.environ.get("FORCESUB_CHANNEL2", "-1002667371758"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#pics
START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/d0831d969b4e19fa286ae-f261f5f392b423f8cd.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/d0831d969b4e19fa286ae-f261f5f392b423f8cd.jpg")

#text
HELP_TXT = "<b>ʜɪ ᴅᴜᴅᴇ!!\nᴛʜɪs ɪs ᴀ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ ᴡʜɪᴄʜ ᴏɴʟʏ ᴡᴏʀᴋ ғᴏʀ : [ @Cultured_Aodox ]\n\n❏ ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs\n├/start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ\n├/about : ᴏᴜʀ Iɴғᴏʀᴍᴀᴛɪᴏɴ\n└/help : ʜᴇʟᴘ ʀᴇʟᴀᴛᴇᴅ ʙᴏᴛ\n\n💥 sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ʙᴏᴛʜ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!\n\n🧑‍💻 ᴏᴡɴᴇᴅ ʙʏ : [ @Cultured_Aodox ]</b>"
ABOUT_TXT = "<blockquote><b><i>» ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/Urr_Sanjiii>➳≛⃝Sanjii</a>\n» 𝐀ɴɪᴍᴇ 𝐂ʜᴀɴɴᴇʟ : <a href=https://t.me/anime_Aodox>ᴀɴɪᴍᴇ ᴀᴏᴅᴏx</a>\n ›› ᴡᴇʙsᴇʀɪᴇs : <a href=https://t.me/webseries_unity>ᴡᴇʙsᴇʀɪᴇs</a>\n»  ᴀᴅᴜʟᴛ ᴄʜᴀɴɴᴇʟs : <a href=https://t.me/Cultured_Aodox>ᴄᴏʀɴʜᴜʙ</a>\n» ᴄᴏᴍᴍᴜɴɪᴛʏ : <a href=https://t.me/novadise>ɴᴏᴠᴀᴅɪsᴇ</a>\n» ᴏᴡɴᴇʀ : <a href=https://t.me/Diablovolfir0>𝘿𝙄𝘼𝘽𝙇𝙊</i></b></blockquote>"
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜɪ ᴛʜᴇʀᴇ... {first}! 💥\n\nɪ ᴀᴍ ᴀ ꜰɪʟᴇ ꜱᴛᴏʀᴇ ʙᴏᴛ...!\nɪ ᴄᴀɴ ᴘʀᴏᴠɪᴅᴇ ᴘʀɪᴠᴀᴛᴇ ꜰɪʟᴇꜱ ᴛʜʀᴏᴜɢʜ ᴀ ꜱᴘᴇᴄɪꜰɪᴄ ʟɪɴᴋ....!\n\nᴅᴇᴠᴇʟᴏᴘᴇᴅ ғᴏʀ : [ @Cultured_Aodox ] </b>")
try:
    ADMINS=[7827448605]
    for x in (os.environ.get("ADMINS", "1683225887 7252834931 7813956229 5879656694").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {first}!⚡\n\n🫧ᴘʟᴇᴀꜱᴇ ᴊᴏɪɴ ʙᴏᴛʜ ᴏꜰ ᴏᴜʀ ᴄʜᴀɴɴᴇʟꜱ ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ...!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

#Short Url or Api
SHORT_URL = os.environ.get("SHORTNER_URL", "linkshortify.com")
SHORT_API = os.environ.get("SHORTNER_API", "7a541402aeacbdbff361696add89bce2cf8afa4e")

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "Pʟᴇᴀꜱᴇ ᴅᴏɴ'ᴛ ᴍᴇꜱꜱᴀɢᴇ ᴍᴇ ᴅɪʀᴇᴄᴛʟʏ ɪ ᴀᴍ ᴏɴʟʏ ᴡᴏʀᴋ ꜰᴏʀ - [@Cultured_Aodox]"

AUTO_DEL = os.environ.get("AUTO_DEL", "True")
DEL_TIMER = int(os.environ.get("DEL_TIMER", "1800"))
DEL_MSG = "<b>This File is deleting automatically in {time}. Forward in your Saved Messages..!</b>"

ADMINS.append(OWNER_ID)
ADMINS.append(7827448605)

LOG_FILE_NAME = "sanjiisama.txt"

LOG_FILE_NAME = "sanjiisama.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)

#Bhen ke lavdo Credit hataya na ma choddunga wahi aakr salo use karo bas 
