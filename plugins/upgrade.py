from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup, ForceReply) 
from pyrogram import Client, filters

@Client.on_callback_query(filters.regex('upgrade'))
async def upgrade(bot, update):
    text = """**Uᴛɪʟɪsᴀᴛᴇᴜʀ Pʟᴀɴ Fʀᴀɪᴛ**
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 2 Gᴏ
    Pʀɪx : 0
    
    **🪙 Bᴀsɪqᴜᴇ** 
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 20 Gᴏ
    Pʀɪx : 🌎 0.59$ pᴀʀ mᴏɴᴛʜ
    
    **⚡ Sᴛᴀɴᴅᴀʀᴅ**
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 50 Gᴏ
    Pʀɪx : 🌎 1.19$ pᴀʀ mᴏɴᴛʜ
    
    **💎 Pʀᴏ**
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 100 Gᴏ
    Pʀɪx : 🌎 2.16$ pᴀʀ mᴏɴᴛʜ
    
    💎 ᴇᴄʜᴀɴɢᴇʀ ᴠᴏꜱ ᴇᴛᴏɪʟᴇꜱ ᴛᴇʟᴇɢʀᴀᴍ ᴘᴏᴜʀ ᴀᴠᴏɪʀ ᴅᴇꜱ ᴘʟᴀɴ ᴘʀᴇᴍɪᴜᴍ
    ᴀᴘʀès pᴀʏᴇᴍᴇɴt, ᴇɴᴠᴏʏᴇᴢ ᴜɴᴇ Cᴀᴘᴛᴜʀᴇ Dᴇ Lᴇ Pᴀʏᴇᴍᴇɴt Dᴜ Pᴀʏᴇᴜʀ ᴀ L'ᴀᴅmɪɴ @hyoshdesign"""
    
    keybord = InlineKeyboardMarkup([[ 
                InlineKeyboardButton("Aᴅᴍɪɴ", url = "https://t.me/hyoshdesign")], 
                [InlineKeyboardButton("Aɴɴᴜʟᴇʀ", callback_data = "cancel")]])

    await update.message.edit(text = text, reply_markup = keybord)

@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot, message):
    text = """**Uᴛɪʟɪsᴀᴛᴇᴜʀ Pʟᴀɴ Fʀᴀɪᴛ**
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇ : 2 Gᴏ
    Pʀɪx : 0
    
    **🪙 Bᴀsɪqᴜᴇ** 
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 20 Gᴏ
    Pʀɪx :🌎 0.59$ pᴀʀ mᴏɴᴛʜ
    
    **⚡ Sᴛᴀɴᴅᴀʀᴅ**
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 50 Gᴦ
    Pʀɪx : 🌎 1.19$ pᴀʀ mᴏɴᴛʜ
    
    **💎 Pʀᴏ**
    Lɪᴍɪᴛᴇ Dᴇ Dᴇ́sᴛɪɴᴀᴛɪᴏɴ Qᴜᴏᴛɪᴅɪᴇɴ : 100 Gᴏ
    Pʀɪx : 🌎 2.16$ pᴀʀ mᴏɴᴛʜ
    
    💎 ᴇᴄʜᴀɴɢᴇʀ ᴠᴏꜱ ᴇᴛᴏɪʟᴇꜱ ᴛᴇʟᴇɢʀᴀᴍ ᴘᴏᴜʀ ᴀᴠᴏɪʀ ᴅᴇꜱ ᴘʟᴀɴ ᴘʀᴇᴍɪᴜᴍ
    ᴀᴘʀès pᴀʏᴇᴍᴇɴt, ᴇɴᴠᴏʏᴇᴢ ᴜɴᴇ Cᴀᴘᴛᴜʀᴇ Dᴇ Lᴇ Pᴀʏᴇᴍᴇɴt Dᴜ Pᴀʏᴇᴜʀ ᴀ L'ᴀᴅmɪɴ @Hyoshdesign"""
    
    keybord = InlineKeyboardMarkup([[ 
                InlineKeyboardButton("Aᴅᴍɪɴ", url = "https://t.me/hyoshdesign")], 
                [InlineKeyboardButton("Aɴɴᴜʟᴇʀ", callback_data = "cancel")]])

    await message.reply_text(text = text, reply_markup = keybord)
