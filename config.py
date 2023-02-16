## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME, "BQAk_LRNZwYythFCkjGStPNOBeyDx3L4aZXemPrZbYqo_3WiIE8pj_hywFpOUrUYF24r6jxot7zc73BDP6I8aIfxvAHVv2PPFCWe2aTk2jklO0aT53OTktos70svL3MLd3RkmnddUZEMHofof6tgyl-VjBLxNPgrTZ4bU8OF7CNajFLJ07IX8tOC_LYTGqx-tFo4Zi7K3aaU8taM_lBcI8xrbR6i4cjZVdOtS0MiHtDyLiXPCwkqp9CKZ_DgZVHxuihsYCxnXt1FYhCMdsRYJniDasdYGIK6pC78my4tWb6inORVtBs1LIUTUfOpDGsODXo4JF1A5V42geDJtgnnkZxIazRIhQA")
BOT_TOKEN = getenv("BOT_TOKEN", "5920443941:AAG1UJMR9X7QvM-wUH617Bz8pU-MRqlpM8E")
BOT_NAME = getenv("BOT_NAME", "LalluMusicBot")
API_ID = int(getenv("API_ID", "18286764"))
API_HASH = getenv("API_HASH", "f88e25386cd833a66d15a08d6bc30351")
OWNER_NAME = getenv("OWNER_NAME", "Thavaraj")
OWNER_USERNAME = getenv("OWNER_USERNAME", "thavarajtj")
ALIVE_NAME = getenv("ALIVE_NAME", "Lallu")
BOT_USERNAME = getenv("BOT_USERNAME", "LalluMusicBot")
OWNER_ID = getenv("OWNER_ID", "1471469091")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "LalluMusicBot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TAMILCHATS_MAKKAL")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "Alinallmovies")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1471469091").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
START_PIC = getenv("START_PIC", "https://telegra.ph/file/2c23f012984fa91267146.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/S780821/Flame-Music")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/c540aac0249486854787b.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/6f1cfec700087f6fcb391.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/c3547532105a0cb67229d.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/be5f551acb116292d15ec.png")
IMG_5 = getenv("IMG_5", "https://telegra.ph/file/c3401a572375b569138c3.png")
IMG_6 = getenv("IMG_6", "https://telegra.ph/file/c3401a572375b569138c3.png")
