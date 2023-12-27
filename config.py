import os
from os import getenv


API_ID = int(getenv("API_ID", "26405281"))
API_HASH = getenv("API_HASH", "77b54622ef8e0fd15555d939fc74005d")
BOT_USERNAME = getenv("BOT_USERNAME", "papaxdd_bot")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "test_supportchat")
LOG_CHANNEL = int(getenv("LOG_CHANNEL", "-1001976068632"))
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "6236671629:AAGUod3DN_hhNITz87h8v8_KEBjZrvAdqRA")
OWNER_ID = int(getenv("OWNER_ID", "6058139652"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6058139652").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://sano07:sano07@cluster0.jxywgnn.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "BQClHu8Aj_jwqNrsaoG_jmHZQK80vf9nq9KwlkPO2fJ1zfzzhkeXrnn62LnEJDToFeFTCoMwfmrpmil4_tnWzACKrHbOIiIaarQ6alieDm9OYvuoiaZUi9BjRPmw1DRlq4zBLceOa-_uCp9edAMHY_7-priif2ZAH0SDO1q3ustZVz639cEZMOtftVUJWciOTyV6YoR-VxaD4NJ7WvG2e4EmAILsTIYOaui31jRFiSMELClo0pP0dANvuGnfCE7YwZ7rFloOqvb5eW2SEKxmwakTBH2Baftj46dIOwzXBR8qk5kjoGKwlZipgnfQaDTYFIILXFh7yIbdx2njLat4oQ-qpt3aHgAAAAF09ByuAA")
ARQ_API_URL = getenv("ARQ_API_URL", "arq.hamker.dev")
ARQ_API_KEY = getenv("ARQ_API_KEY", "TQNXUE-EUDMWA-XPSHTG-JFAFWC-ARQ")
