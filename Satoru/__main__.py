import asyncio
import importlib
from pyrogram import idle
from Satoru import app
from Satoru.functions import ALL_FUNCTIONS

 

loop = asyncio.get_event_loop()


async def satoru_boot():
    for all_functions in ALL_FUNCTIONS:
        importlib.import_module("Satoru.functions." + all_functions)
    print("ʙᴏᴛ ꜱᴛᴀʀᴛᴇᴅ ꜱᴜᴄᴄᴇꜱꜱꜰᴜʟʟʏ ⎋")
    await idle()
    print("⎌ ꜱᴛᴏᴘᴘɪɴɢ ʙᴏᴛ")


if __name__ == "__main__":
    loop.run_until_complete(satoru_boot())
