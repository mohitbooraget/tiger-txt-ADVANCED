import os

API_ID = API_ID = 23291931

API_HASH = os.environ.get("API_HASH", "4b11dd648188731fb7c9bc8083e8791c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7036028043:AAFV4abeqHOUwN9KnqQfKZyg7Izy3if_H2g")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6594402123))

LOG = -1002079896558

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "5987970971").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


