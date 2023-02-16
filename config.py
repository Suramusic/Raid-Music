## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME, "BQEXCKwAXqk4HhKtxCM9Wo6moGonHQEMdG1e5uSZByeNwrPm_HMoQoeCCArFJF4PLbPqp5NPlKNVeaaSHQktG7yAiwGIiH2IqC6Dpeq0teJ7gc9TLGYhVViNW__Nrgj-Y20XCFdwst2XTqYCo_9vFJZ1pooyxA9hciA5in-kXe_OpZi4V5sznsesSh-kN0-As-_AYUmsX6GkTYmDfmpYxA1Xll5eBnQ17R56gteyguRb3f8O8in3Dv-VvBRVyAHioa33BW8-FJlBkJcO7hv5U9VjhT403uWyjkzqc5dBOYcAl8Kz-gEZn4Qcu7alf8_T9GRoWC0weZO0uJ0Bsp-JL2ZPhIXJKQAAAAExDRpeAA")
BOT_TOKEN = getenv("BOT_TOKEN", "5920443941:AAG1UJMR9X7QvM-wUH617Bz8pU-MRqlpM8E")
BOT_NAME = getenv("BOT_NAME", "LalluMusicBot")jdjd
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
