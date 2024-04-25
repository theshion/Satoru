import asyncio
import random
from pyrogram import Client, enums
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import filters
from pyrogram.enums import ChatType
from Satoru import app
from config import BOT_USERNAME

START_IMG = (
    "https://telegra.ph/file/84081fe2722a5357fee01.jpg",
    "https://telegra.ph/file/926d9a276831e88075142.jpg",
)

START_TEXT = """
ʜᴇʏᴏ [{}](tg://user?id={}) 

⎌ 𝙸'ᴍ ɢᴏᴊᴏ ꜱᴀᴛᴏʀᴜ ᴛʜᴇ ꜱᴜᴘʀᴇᴍᴇ ᴀ.ɪ ᴅᴇꜱɪɢɴᴇᴅ ᴛᴏ ᴇɴʜᴀɴᴄᴇ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴡɪᴛʜ ᴀɴɪᴍᴇ ꜰᴇᴀᴛᴜʀᴇꜱ ᴀɴᴅ ᴀ ꜱᴇᴀᴍʟᴇꜱꜱ ᴍᴜꜱɪᴄ ᴇxᴘᴇʀɪᴇɴᴄᴇ.
⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯
⌥ ᴄᴏɴᴛᴀɪɴ ᴇɴʜᴀɴᴄᴇ ꜰᴜɴᴄᴛɪᴏɴꜱ ʟɪᴋᴇ ɢᴇɴᴅᴇʀ, ᴡᴀɪꜰᴜ'ꜱ, ᴍᴜꜱɪᴄ-ᴜɴɪᴛ, ʀᴀᴘɪᴅᴄʜᴇᴄᴋ ᴇxᴛʀᴀ!
╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶╶
▸ ʙʏ ᴄʟɪᴄᴋɪɴɢ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴀᴄᴄᴇꜱꜱ ʙᴏᴛ ꜰᴇᴀᴛᴜʀᴇꜱ ꜰᴏʀ ʏᴏᴜᴛ ɢʀᴏᴜᴘ ʙᴇɴᴇꜰɪᴛꜱ.
"""

@app.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("ᴇɴʀɪᴄʜ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɴᴏᴡ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/AC_Anime_Group"),
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/GodlyEmperor"),
        ],
        [
            InlineKeyboardButton("ꜰᴜɴᴄᴛɪᴏɴꜱ", callback_data="help_"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(buttons)
    if message.chat.type == ChatType.PRIVATE:
        msg = await message.reply_photo(
            photo=random.choice(START_IMG),
            caption="◾◽◽", reply_markup=None)
        await asyncio.sleep(0.1)
        await msg.edit_caption("◾◾◽", reply_markup=None)
        await asyncio.sleep(0.1)
        await msg.edit_caption("◾◾◾", reply_markup=None)
        await asyncio.sleep(0.1)
        await msg.edit_caption(START_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)
    else:
        btn = InlineKeyboardMarkup([[
            InlineKeyboardButton("ꜱᴛᴀʀᴛ ᴍᴇ ɪᴍ ᴘʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ", url=f"http://t.me/{BOT_USERNAME}?start")]])
        await message.reply(
            f"ʜᴇʏ {message.from_user.mention} ᴘᴍ ᴍᴇ ɪғ ʏᴏᴜ ɪɴᴛʀᴇsᴛᴇᴅ.",
            reply_markup=btn
        )
