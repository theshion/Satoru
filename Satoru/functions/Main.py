import asyncio
import random
from pyrogram import Client, InlineKeyboardButton, InlineKeyboardMarkup, enums
from pyrogram.types import Message
from pyrogram import filters
from pyrogram.enums import ChatType
from Satoru import app
from config import BOT_USERNAME



@app.on_message(filters.command(["start"], prefixes=["/", "!"]))
async def start(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton("ᴇɴʀɪᴄʜ ʏᴏᴜʀ ɢʀᴏᴜᴘ ɴᴏᴡ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
        ],
        [
            InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/nexius_support"),
            InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ", url="https://t.me/fatherOfpaul"),
        ],
        [
            InlineKeyboardButton("ꜰᴜɴᴄᴛɪᴏɴꜱ", callback_data="help_"),
        ],
        [
            InlineKeyboardButton("ᴍᴜꜱɪᴄ-ᴜɴɪᴛ", callback_data="mhelp_")
        ]
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

app.run()
