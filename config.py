# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "244147"))
API_HASH = getenv("API_HASH", "350b3b383bd453a2060d9dcccb9ecb")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "8176451634").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://:EhXvJKdpq6FdzHO2@cluster0.x4ika.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002347610797")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002182888803"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
