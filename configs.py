import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "26506890"))
    API_HASH = os.environ.get("API_HASH", "5839207dcf3b270c58d88d5de6830bac")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5883676435:AAGJ3UbHTGySx185h-_pZMOcxvg5ENQn9yE")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "LinkSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "BQC0h_VjsgoS5NHwUt8-JPE8DAFT-ibzQD0Lt3AXEllN9DbSEDW45O3-3MH599T-drab1CmCG98pJBU5muqIOxgyWwsBq0nzHqWLL7sPvbB_d087jSzNr9fd0rrR7E1DphZ9pdlToAhgttFI79uo00hL6KlrlDXfZH4UWBTOB4sV9MIaPBv27-RebkKdFmD0bRK1vmuEROksFznY8lcgWAOgPzeT861uMzqOKE0D8SqjllWC4LPuahCwj4edrEOaqDG3-aaltIEPcqasfefUxZw_uTF0fFr_2d1SUmGs-ZbCPKfRMUoFI-PZoMEWuouKg52Ry0D8Umc6zrquX_tULq3aAAAAAUoOq68A")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001685615060"))
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Mdsik_moviebot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "5537442735"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Mdsikmoviebot:Mdsikmoviebot@cluster0.xwbcpg3.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "updates_channel_link")
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

<a>Made With ❤ By @updates_channel_link</a></b>
"""


    START_MSG = """
<b>Hey! {}😅,

I'm Link Search Bot.🤖

I Can Search 🔍 What You Want❗

<a>Made With ❤ By @updates_channel_link</a></b>
"""

