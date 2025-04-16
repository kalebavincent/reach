import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
OWNER = int(os.getenv("OWNER", ""))
BOT_USERNAME = os.getenv('BOT_USERNAME', "")

FORCE_SUBS = os.getenv("FORCE_SUBS", "-1002049629020")
LOG_CHANNEL = int(os.getenv("LOG_CHANNEL"))
DEFAUTTHUMB = os.getenv("DEFAUTTHUMB", "")

DB_URL = os.getenv("DB_URL", "")
DB_NAME = os.getenv("DB_NAME", "")
IMG_FOLDER = os.environ.get("IMG_FOLDER", "./path")

STRING = os.getenv("STRING", "")
BOT_PIC = os.getenv("BOT_PIC", "https://graph.org/file/cca849a2f63053fa3f622.jpg")

SHORTNER_URL = os.getenv("SHORTNER_URL", "")
SHORTNER_API = os.getenv("SHORTNER_API", "")
TOKEN_TIMEOUT = os.getenv("TOKEN_TIMEOUT", "")
