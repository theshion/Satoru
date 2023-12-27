import time
import random
from asyncio import sleep as rest
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from Satoru import boot as tim
from Satoru import app
from config import OWNER_ID as owner
from config import SUDO_USERS as sudo
from pyrogram import __version__
from platform import python_version

lul = [819560568]

# ------------------------------------------------------------------------------- #

photo = [
    "https://telegra.ph/file/60e757cb0d8836fa8255d.jpg"
]

# ------------------------------------------------------------------------------- #

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["𝚂", "𝙼", "𝙷", "𝙳𝙰𝚈𝚂"]

    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time

sudo.append(owner)

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command(["ping"], prefixes=["/", "!"]))
async def ping(_, m: Message):
    start_time = time.time()
    sender = m.from_user
    up = get_readable_time((time.time() - tim))
    end_time = time.time()
    ping1 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    
    if m.from_user.id not in lul:
        e = await m.reply_photo(photo=random.choice(photo), caption="**ᴘɪɴɢ ᴇᴠᴇɴᴛ**")
        await e.edit_text(PING_TEXT.format(ping1, up, __version__))
    else:
        await m.reply(PING_TEXT.format(ping1, up, __version__))

# ------------------------------------------------------------------------------- #

PING_TEXT = """
╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴
⬝ **ꜱᴘᴇᴇᴅ ᴏꜰ ᴀɪ⥮ -** `{}`
⬝ **ʙᴏᴛ ᴜᴘᴛɪᴍᴇ -** `{}`
⬝ **ᴘʏᴛʜᴏɴ ᴠᴇʀsɪᴏɴ -** `3.11.12`
⬝ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ -** `{}`
⬝ **ᴘᴛʙ ᴠᴇʀꜱɪᴏɴ -** `20.6`
╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴╶╴
"""
# ------------------------------------------------------------------------------- #

Button = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close_data")]
    ]
)

# ------------------------------------------------------------------------------- #

@app.on_message(filters.command("alive"))
async def alive(_, msg: Message):
    start_time = time.time()
    sender = msg.from_user
    up = get_readable_time((time.time() - tim))
    end_time = time.time()
    ping1 = str(round((end_time - start_time) * 1000, 3)) + " ms"
    x = await msg.reply_photo(photo=random.choice(photo), caption="**ᴀʟɪᴠᴇ**")
    await x.edit_caption(
        "╺╸╺╸╺╸╺╸╺╸╺╸╺╸╺╸╺╸╺╸╺╸\n**⎌  ɢᴏᴊᴏ ꜱᴀᴛᴏʀᴜ ɪꜱ ᴀʟɪᴠᴇ**\n\n"
        "**⬝ ᴍᴀɴᴀɢɪɴɢ ɢʀᴏᴜᴘ ꜱɪɴᴄᴇ -**  `{}`\n"
        "**⬝ ᴡᴏʀᴋɪɴɢ ᴡɪᴛʜ ᴛʜᴇ ᴘɪɴɢ ᴏꜰ -** `{}`\n"
        "**⬝ ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ -** `2.0.106`\n"
        "**⬝ ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ -** [ɢᴏᴊᴏ ꜱᴀᴛᴏʀᴜ](https://t.me/Gojo_Satoru_botx)\n"
        "**⬝ ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ -** `3.11.12`\n╺╸╺╸╺╸╺╸╺╸╺╸╺╸╺╸╺╸".format(up, ping1)
    )

# ------------------------------------------------------------------------------- #
