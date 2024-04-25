import logging
from pyrogram import Client, filters
from pyrogram.types import *

app = Client("my_bot")

FORBIDDEN_KEYWORDS = ["porn", "xxx", "sex", "NCERT", "XII", "page", "Ans", "meiotic", "divisions", "System.in", "Scanner", "void", "nextInt"]

@app.on_message()
async def handle_message(client, message):
    global user_mention
    if any(keyword in message.text for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"✦ Deleting message with ID {message.message_id}")
        await message.delete()
        user_mention = message.from_user.mention
        await message.reply_text(f"✦ Hey {user_mention}, please refrain from using forbidden keywords.")

    if any(keyword in message.caption for keyword in FORBIDDEN_KEYWORDS):
        logging.info(f"✦ Deleting message with ID {message.message_id}")
        await message.delete()
        user_mention = message.from_user.mention
        await message.reply_text(f"✦ Hey {user_mention}, please refrain from using forbidden keywords in captions.")

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()

def delete_long_messages(_, m):
    return len(m.text.split()) > 400

@app.on_message(filters.group & filters.private & delete_long_messages)
async def delete_and_reply(_, msg):
    await msg.delete()
    user_mention = msg.from_user.mention
    await app.send_message(msg.chat.id, f"✦ Hey {user_mention}, please keep your message short.")

async def delete_pdf_files(client, message):
    global user_mention
    if message.document and message.document.mime_type == "application/pdf":
        user_mention = message.from_user.mention
        warning_message = f"✦ Hey {user_mention}, please refrain from sending PDF files for copyright reasons."
        await message.reply_text(warning_message)
        await message.delete()

@app.on_message(filters.group & filters.document)
async def message_handler(client, message):
    await delete_pdf_files(client, message)

try:
    app.start()

except KeyboardInterrupt:
    print("KeyboardInterrupt detected, stopping...")
    app.stop()

finally:
    pass
