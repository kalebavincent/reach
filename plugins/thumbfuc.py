from pyrogram import Client, filters 
from helper.database import find, delthumb, addthumb, viewthumb

@Client.on_message(filters.private & filters.command(['viewthumb']))
async def viewthumbs(client, message):
    print(message.chat.id)
    thumb = find(int(message.chat.id))[0]
    if thumb:
        await client.send_photo(message.chat.id, photo=f"{thumb}")
    else:
        await message.reply_text("😔 __**ᴠᴏᴜꜱ ɴ'ᴀᴠᴇᴢ ᴘᴀꜱ ᴅᴇ ᴠɪɢɴᴇᴛᴛᴇ**__")

@Client.on_message(filters.private & filters.command(['delthumb']))
async def removethumb(client, message):
    delthumb(int(message.chat.id))
    await message.reply_text("❌️ __**ᴠᴏᴛʀᴇ ᴠɪɢɴᴇᴛᴛᴇ ᴀ éᴛé ꜱᴜᴘᴘʀɪᴍéᴇ ᴀᴠᴇᴄ ꜱᴜᴄᴄèꜱ**__")

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client, message):
    file_id = str(message.photo.file_id)
    addthumb(message.chat.id, file_id)
    await message.reply_text("✅️ __**ᴠᴏᴛʀᴇ ᴠɪɢɴᴇᴛᴛᴇ ᴀ éᴛé ᴇɴʀᴇɢɪꜱᴛʀéᴇ ᴀᴠᴇᴄ ꜱᴜᴄᴄèꜱ**__")
