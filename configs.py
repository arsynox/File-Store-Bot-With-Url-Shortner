import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "27404976"))
  API_HASH = os.environ.get("API_HASH", "b9a6f7abf66013a54ec73319806adbe7")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "8154077368:AAH55sgVEpit18oIRsDpoZeE0V_ZE6EM5qE")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "arsy_url_bot")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "-1002146953908"))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "shrinkme.io")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "b029ef05d2d0000b4ee9deffe0d9f86b650b5c0d")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "6822491887"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://arsynox:arsynox#90@cluster0.rllegme.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002638392397")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002896373732"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [FileStore Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Library: [Pyrogram](https://docs.pyrogram.org)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [ARSYNOX](https://telegram.me/pheonixion)
 
 I am Super noob Please Support My Hard Work.

[Donate Me](https://t.me/pheonixion)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **FileStore Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
