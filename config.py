# safe_repo
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://meenakanhaiyalal638:files@files.8ko8k.mongodb.net/?retryWrites=true&w=majority&appName=files")
LOG_GROUP = getenv("LOG_GROUP", "-1002350813151")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002375692750"))
