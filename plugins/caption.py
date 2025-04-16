from pyrogram import Client, filters  
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from helper.database import *
from helper.font import FontConverter

@Client.on_message(filters.private & filters.command('set_caption'))
async def add_caption(client, message):
    if len(message.command) == 1:
       return await message.reply_text("**ᴠᴏᴛʀᴇ ᴄᴀᴘᴛɪᴏɴ ᴘᴏᴜʀ ᴇᴛʀᴇ ᴀᴅᴅᴇᴇ.\n\nᴇxᴀᴍᴘʟᴇ :- `/set_caption 📕 ɴᴀᴍᴇ ➠ : {filename} \n\n🔗 sɪᴢᴇ ➠ : {filesize} \n\n⏰ dᴜʀᴀᴛɪᴏɴ ➠ : {duration}`**")
    caption = message.text.split(" ", 1)[1]
    addcaption(int(message.chat.id), caption)
    await message.reply_text("**ᴠᴏᴛʀᴇ ᴄᴀᴘᴛɪᴏɴ ᴇꜱᴛ ᴇɴʀᴇɢɪꜱᴛʀᴇʀ ᴀᴠᴇᴄ ꜱᴜᴄᴄᴇᴇꜱ ✅**")

@Client.on_message(filters.private & filters.command('del_caption'))
async def delete_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if not caption:
        await message.reply_text("**ᴠᴏᴛʀᴇ ᴄᴀᴘᴛɪᴏɴ ᴅᴇsᴛɪɴᴇᴇ ɴ'ᴇxɪsᴛᴇ ᴘᴀs ❌**")
        return
    delcaption(int(message.chat.id))
    await message.reply_text("**ᴠᴏᴛʀᴇ ᴄᴀᴘᴛɪᴏɴ ᴀ ᴇᴛᴇ ꜱᴜᴘᴘʀɪᴍᴇʀ ᴄᴏᴍᴘʟᴇᴛᴇᴍᴇɴᴛ 🗑️**")
                                       
@Client.on_message(filters.private & filters.command('see_caption'))
async def see_caption(client, message): 
    caption = find(int(message.chat.id))[1]
    if caption:
       await message.reply_text(f"<b><u>ᴠᴏᴛʀᴇ ᴄᴀᴘᴛɪᴏɴ:</b></u>\n\n`{caption}`")
    else:
       await message.reply_text("**ᴠᴏᴛʀᴇ ᴄᴀᴘᴛɪᴏɴ ᴅᴇsᴛɪɴᴇᴇ ɴ'ᴇxɪsᴛᴇ ᴘᴀs ❌**")

from pyrogram import Client, filters

@Client.on_message(filters.private & filters.command('set_font'))
async def set_font(client, message):
    if len(message.command) == 1: 
        t_unicode = FontConverter("En Unicode").convert("En Unicode", "unicode")
        t_bubble = FontConverter("En Bubble").convert("En Bubble", "bubble")
        t_bold = FontConverter("En Bold").convert("En Bold", "bold")
        t_strike = FontConverter("En Strike").convert("En Strike", "strikethrough")
        t_reverse = FontConverter("En Reverse").convert("En Reverse", "reverse")
        t_script = FontConverter("En Script").convert("En Script", "script")
        
        return await message.reply_text(f"Voici les fonts disponibles : \n\n"
                                       f"🔠 `Unicode` : {t_unicode} \n"
                                       f"💬 `Bubble` : {t_bubble} \n"
                                       f"🔤 `Bold` : {t_bold} \n"
                                       f"✂️ `Strike` : {t_strike} \n"
                                       f"↺️ `Reverse` : {t_reverse} \n"
                                       f"📜 `Script` : {t_script} \n\n"
                                       f"Ex : `/set_font Unicode`")
    
    available_fonts = ["unicode", "bubble", "bold", "italic", "underline", "strikethrough", "reverse", "script"]
    
    if len(message.command) > 1:
        font = message.command[1].lower()  
        if font not in available_fonts:
            return await message.reply_text(f"Police invalide. Voici les polices disponibles : \n\n"
                                           f"🔠 `Unicode` \n💬 `Bubble` \n🔤 `Bold` \n✂️ `Strike` \n↺️ `Reverse` \n📜 `Script` \n\n"
                                           f"Veuillez réessayer avec une police valide.")

        addwatermarkfont(int(message.chat.id), font)
        await message.reply_text("**ᴠᴏᴛʀᴇ font ᴇꜱᴛ ᴇɴʀᴇɢɪꜱᴛʀᴇʀ ᴀᴠᴇᴄ ꜱᴜᴄᴄᴇᴇꜱ ✅**")



@Client.on_message(filters.private & filters.command('del_font'))
async def delete_font(client, message): 
    font = find(int(message.chat.id))[2]
    
    if not font:
        await message.reply_text("**ᴠᴏᴛʀᴇ ᴘᴏʟɪᴄᴇ ᴅᴇsᴛɪɴᴇᴇ ɴ'ᴇxɪsᴛᴇ ᴘᴀs ❌**")
        return
    
    dbcol.update_one({"_id": message.chat.id}, {"$unset": {"watermark_font": ""}})
    
    await message.reply_text("**ᴠᴏᴛʀᴇ ᴘᴏʟɪᴄᴇ ᴀ ᴇᴛᴇ ꜱᴜᴘᴘʀɪᴍᴇʀ ᴄᴏᴍᴘʟᴇᴛᴇᴍᴇɴᴛ 🗑️**")

@Client.on_message(filters.private & filters.command('see_font'))
async def see_font(client, message): 
    font = find(int(message.chat.id))[2]
    
    if font:
        await message.reply_text(f"<b><u>ᴠᴏᴛʀᴇ ᴘᴏʟɪᴄᴇ:</b></u>\n\n`{font}`")
    else:
        await message.reply_text("**ᴠᴏᴛʀᴇ ᴘᴏʟɪᴄᴇ ᴅᴇsᴛɪɴᴇᴇ ɴ'ᴇxɪsᴛᴇ ᴘᴀs ❌**")
