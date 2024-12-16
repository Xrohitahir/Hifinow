# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24497147"))
API_HASH = getenv("API_HASH", "350b3b383bd453a2060d9dcccb9e31cb")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "8176451634"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://irohitahir:1CrmW6nYeQ8nCP2G@cluster0.c2in5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002182888803"))
FORCESUB = getenv("FORCESUB", "-1002347610797")
