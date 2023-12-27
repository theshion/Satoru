import asyncio
import logging
import time
from pyrogram import *
from pytgcalls import PyTgCalls
from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as async_mongo
from importlib import import_module
from os import environ, getenv, listdir, path
from dotenv import load_dotenv
from pyrogram import Client
from config import *
import config
from Python_ARQ import ARQ

loop = asyncio.get_event_loop()
load_dotenv()
boot = time.time()


logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.INFO,
)



app = Client(
    ":app:",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=config.BOT_TOKEN,
)



async_mongo_client = async_mongo(config.MONGO_URL)
db = async_mongo_client.Satoru

print("[INFO]: INITIALZING AIOHTTP SESSION")
aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)

async def app_bot():
    global BOT_ID, BOT_NAME, BOT_USERNAME
    await app.start()
    getme = await app.get_me()
    BOT_ID = getme.id
    BOT_USERNAME = getme.username
    if getme.last_name:
        BOT_NAME = getme.first_name + " " + getme.last_name
    else:
        BOT_NAME = getme.first_name


loop.run_until_complete(app_bot())

