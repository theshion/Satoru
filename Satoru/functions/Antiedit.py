from pyrogram import Client, filters
from pyrogram.types import Message
from Satoru import app

@app.on_edited_message(filters.group & ~filters.me)
async def delete_edited_messages(client, edited_message):
    await edited_message.delete()
