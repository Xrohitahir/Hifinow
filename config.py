# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24497147"))
API_HASH = getenv("API_HASH", "350b3b383bd453a2060d9dcccb9e31cb")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", ""))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "")
LOG_GROUP = int(getenv("LOG_GROUP", ""))
FORCESUB = getenv("FORCESUB", "")
