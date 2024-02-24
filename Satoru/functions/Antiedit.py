import os
from pyrogram import Client, filters
from pyrogram.types import Message
from Satoru import app

# Maintain edit count for each user
edit_counts = {}

# Owner ID and sudo user ID (who can authorize other users)
owner_id = 6432025901  # Example owner ID
sudo_id = 6432025901   # Example sudo user ID

# List of authorized user IDs
authorized_users = []

# Start command handler
@app.on_message(filters.command("start"))
async def start_command(client, message):
    await message.reply_text("Hello! I'm your Anti-Edit Bot. I will delete any message you edit.")

# Message handler for edited messages
@app.on_edited_message(filters.group)
async def edited_message_handler(client, message):
    await client.delete_messages(chat_id=message.chat.id, message_ids=[message.message_id])

# Command handler for authorizing users
@app.on_message(filters.command("authorize"))
async def authorize_command(client, message):
    # Check if the user is authorized to authorize other users
    if message.from_user.id == owner_id or message.from_user.id == sudo_id:
        # Extract the user ID to authorize
        if len(message.command) == 2:
            user_id = message.command[1]
            try:
                user_id = int(user_id)
                authorized_users.append(user_id)
                await message.reply_text(f"User {user_id} has been authorized to send longer messages.")
            except ValueError:
                await message.reply_text("Invalid user ID provided.")
        else:
            await message.reply_text("Please provide a user ID to authorize.")
