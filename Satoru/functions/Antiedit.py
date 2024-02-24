from pyrogram import Client, filters
from pyrogram.types import Message
from Satoru import app as bot

@bot.on_message(filters.group & filters.text)
def echo(bot, message):
    # Save the original message
    original_text = message.text

    # Send the original message
    sent_message = message.reply_text(original_text)

    # Save the message ID for later reference
    sent_message_id = sent_message.message_id

@bot.on_edited_message(filters.group)
def on_edit(bot, message):
    # Delete the edited message
    bot.delete_messages(chat_id=message.chat.id, message_ids=message.message_id)

    # Notify about the edit
    bot.send_message(
        chat_id=message.chat.id,
        text=f"User {message.from_user.mention} edited a message. Original message deleted."
    )
