import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import SUDO_USERS, COMMAND_HANDLER
from Satoru import app

CLAN = SUDO_USERS


async def extract_user(_, message):
    try:
        if message.reply_to_message and message.reply_to_message.from_user:
            user = message.reply_to_message.from_user
        elif len(message.command) > 1:
            user_id = int(message.command[1])
            user = await app.get_users(user_id)
        else:
            await message.reply_text("Pass a user id or reply to a user's message.")
            return None, None, None

        user_id = user.id
        user_first_name = user.first_name
        user_username = user.username
        mention = user.mention

        return user_id, user_first_name, user_username

    except Exception as e:
        print(f"Error in extract_user: {e}")
        await message.reply_text("Error extracting user information.")
        return None, None, None


@app.on_message(filters.command("ban", COMMAND_HANDLER))
async def ban(_, message):
    reply = message.reply_to_message
    chat_id = message.chat.id
    user_id = message.from_user.id
    msg = await message.reply_text("ʙᴀɴ ᴇᴠᴇɴᴛ")

    if message.chat.type == "private":
        await msg.edit("ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ ᴡᴏʀᴋs ᴏɴ ɢʀᴏᴜᴘ.")
    elif reply:
        try:
            user = reply.from_user
            mention = user.mention
            admin_check = await app.get_chat_member(chat_id, user_id)

            if admin_check.status in ("administrator", "creator"):
                if user.id not in CLAN:
                    try:
                        await message.chat.kick_member(user.id)
                        await message.reply_animation(
                            animation="https://te.legra.ph/file/5f1d1cd13e591d0f3dd0f.mp4",
                            caption=f"<b><u>ʙᴀɴ ᴇᴠᴇɴᴛ</u></b>🚷\n⬝ ᴀᴅᴍɪɴ {message.from_user.mention}\n⬝ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ {mention}",
                        )
                        await msg.delete()
                    except RPCError as e:
                        await msg.edit_text(f"ʙᴇᴇᴘ ʙᴏᴏᴘ ᴇʀʀᴏʀ\n{str(e)}")
                else:
                    await msg.edit_text("ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ᴘᴀʀᴛ ᴏꜰ ᴍʏ ᴄʟᴀɴ ɪ ᴄᴀɴ'ᴛ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴀɢᴀɪɴꜱᴛ ᴛʜɪꜱ ᴜꜱᴇʀ.")
            else:
                await msg.edit_text(
                    "ɪ ᴄᴀɴ'ᴛ ʀᴇꜱᴛʀɪᴄᴛ ᴜꜱᴇʀꜱ, ᴍᴀᴋᴇ ꜱᴜʀᴇ ɪ'ᴍ ᴀɴ ᴀᴅᴍɪɴ & ɪ ʜᴀᴠᴇ ʙᴀɴ ʀɪɢʜᴛꜱ ꜱᴏ ɪ ᴄᴀɴ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ."
                )
        except RPCError as e:
            await msg.edit_text(f"ʙᴇᴇᴘ ʙᴏᴏᴘ ᴇʀʀᴏʀ\n{str(e)}")
    elif len(message.command) > 1:
        try:
            if message.command[1].startswith("@"):
                username = message.command[1][1:]
                user = await app.get_users(username)
                wuser_id = user.id
                mention = user.mention
                user_first_name = user.first_name
            else:
                wuser_id, user_first_name, _ = await extract_user(_, message)

            admin_check = await app.get_chat_member(chat_id, user_id)

            if admin_check.status in ("administrator", "creator"):
                if wuser_id not in CLAN:
                    try:
                        await message.chat.kick_member(wuser_id)
                        await message.reply_animation(
                            animation="https://te.legra.ph/file/5f1d1cd13e591d0f3dd0f.mp4",
                            caption=f"<b><u>ʙᴀɴ ᴇᴠᴇɴᴛ</u></b>🚷\n⬝ ᴀᴅᴍɪɴ {message.from_user.mention}\n⬝ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀ [{user_first_name}](tg://user?id={wuser_id})",
                        )
                        await msg.delete()
                    except RPCError as e:
                        await msg.edit_text(f"ʙᴇᴇᴘ ʙᴏᴏᴘ ᴇʀʀᴏʀ\n{str(e)}")
                else:
                    await msg.edit_text("ᴛʜɪꜱ ɢᴜʏ ɪꜱ ᴀ ᴘᴀʀᴛ ᴏꜰ ᴍʏ ᴄʟᴀɴ ɪ ᴄᴀɴ'ᴛ ᴛᴀᴋᴇ ᴀᴄᴛɪᴏɴ ᴀɢᴀɪɴꜱᴛ ᴛʜɪꜱ ᴜꜱᴇʀ.")
            else:
                await msg.edit_text(
                    "ɪ ᴄᴀɴ'ᴛ ʀᴇꜱᴛʀɪᴄᴛ ᴜꜱᴇʀꜱ, ᴍᴀᴋᴇ ꜱᴜʀᴇ ɪ'ᴍ ᴀɴ ᴀᴅᴍɪɴ & ɪ ʜᴀᴠᴇ ʙᴀɴ ʀɪɢʜᴛꜱ ꜱᴏ ɪ ᴄᴀɴ ᴘᴇʀꜰᴏʀᴍ ᴛʜɪꜱ ᴀᴄᴛɪᴏɴ."
                )
        except RPCError as e:
            await msg.edit_text(f"ʙᴇᴇᴘ ʙᴏᴏᴘ ᴇʀʀᴏʀ\n{str(e)}")
    else:
        await msg.edit_text("ʏᴏᴜ ɴᴇᴇᴅ ᴛᴏ ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴍᴇssᴀɢᴇ ᴏʀ ɢɪᴠᴇ ᴀ ᴜsᴇʀ ɪᴅ ᴏʀ ᴜsᴇʀɴᴀᴍᴇ ᴛᴏ ʙᴀɴ.")
