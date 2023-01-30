import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "26506890"))
    API_HASH = os.environ.get("API_HASH", "5839207dcf3b270c58d88d5de6830bac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5883676435:AAGJ3UbHTGySx185h-_pZMOcxvg5ENQn9yE")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQB3u7M5zaM7MHlN13m-npkVJMyvy8Idvx-k4Opk3VyrFlfpEWeeva1cd2UfWMPKG5EKp_Dzy8c3S0eFYLGEvbzvTX3D-KxQLBDt-TPnuUBCrdtKNcEZEVerNUZ77KqVB55uaQhpYWhAOGv0IaHx1zKJD-5KtA2SkWCmumC4rctUcMcBugIRZwcnh0l7ExVkctktR6f4FelNOL9OmKlV_FWcr3cFRUDRBES2y10tLcvOSfLnWrbGAJLRGmHMzFgzSPMFZ9O2PQONRioHrqp1S9rgYh7DLbnJsxkksqBbJ5pMHLgoI7tW-VW1imoPnecaVc3IAPrZWYXUsZxPwkc1or3pAAAAAUoOq68A")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001685615060"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdsik_moviebot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5537442735"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Mdsikmoviebot:Mdsikmoviebot@cluster0.xwbcpg3.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "Bot_channel_12")
    ABOUT_BOT_TEXT = """<b>This is Link Search Bot.
    
    
    
🤖 My Name: <a href='https://youtube.com/@GreyMattersYT'>Link Search Bot</a>

📝 Language : <a href='https://www.python.org'> Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'> Pyrogram</a>

📡 Server: <a href='koyeb.com'>Koyeb</a>

👨‍💻 Created By: <a href='https://t.me/GreyMatter_owner'>GreyMatters</a></b>
"""

    ABOUT_HELP_TEXT = """<b>👨‍💻 Creator : <a href='https://t.me/GreyMatter_Owner'>GreyMatters</a>
If You Want Your Own Bot Like This Then You Can Contact Our Creator.</b>
"""

    HOME_TEXT = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Bot_channel_12</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @Bot_channel_12</a></b>
"""

