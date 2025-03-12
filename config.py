# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport


import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7978441369:AAHxSmz78-4Ar-QxsiLnzqC18ANs9JUmssI")
#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "22005506"))
#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "af9406c860b34bd575b04f2b555bb6b0")
#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002437677949"))
# NAMA OWNER
OWNER = os.environ.get("OWNER", "sewxiy")
#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7840367398"))
#Port
PORT = os.environ.get("PORT", "8030")
#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://xeroxbayzid12:xeroxbayzid12@cluster0.dcapc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Time in seconds for message delete, put 0 to never delete
TIME = int(os.environ.get("TIME", "7200"))


#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "-1002201154798"))
#put 0 to disable
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))#put 0 to disable
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "0"))#put 0 to disable
FORCE_SUB_CHANNEL4 = int(os.environ.get("FORCE_SUB_CHANNEL4", "0"))#put 0 to disable

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://i.postimg.cc/QMt64QyK/1737020082864.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.postimg.cc/QMt64QyK/1737020082864.jpg")

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
TOKEN = True if os.environ.get('TOKEN', "False") == "True" else False 
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 600)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "False")
TUT_VID = os.environ.get("TUT_VID","")


HELP_TXT = "- Assalamu Alaikum, I'm a Blmbd.Click Official File Store Bot…!☠️\n\n- I Can't Help You, Because This Bot Is Personal, Everyone Can't Use It…!\n\n- Made By : <a href='https://t.me/xerox_bayzid'>BAYZ!D / بیخیر 🤧</a>\n\n🌟 Visit Our Site : https://blmbd.click"

ABOUT_TXT = "- Assalamu Alaikum, I'm a Blmbd.Click Official File Store Bot…!☠️\n\n- I Will Save All Blmbd.Click Telegram Files and Provide Them To Users…!\n\n- Made By : <a href='https://t.me/xerox_bayzid'>BAYZ!D / بیخیر 🤧</a>\n\n🌟 Visit Our Site : https://blmbd.click"


START_MSG = os.environ.get("START_MESSAGE", "- Welcome To Blmbd.Click Official File Store Bot…!☠️\n\n- Kindly Join Us our Telegram Channel To Access The Bot…!👻\n\n🌟 Visit Our Site : https://blmbd.click")
try:
    ADMINS=[5548923721]
    for x in (os.environ.get("ADMINS", "5548923721").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "- Welcome To Blmbd.Click Official File Store Bot…!☠️\n\n- Kindly Join Us our Telegram Channel To Get Your Desired File…!👻\n\n🌟 Visit Our Site : https://blmbd.click")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "{previouscaption} <b>- By : https://blmbd.click</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "{uptime}"
USER_REPLY_TEXT = "File Token is Empty or Expired. Get New File Token."

ADMINS.append(OWNER_ID)
ADMINS.append(7840367398)

LOG_FILE_NAME = "filesharingbot.txt"

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
   
