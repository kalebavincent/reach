from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from config import *
from pyrogram import Client, filters
from helper.date import add_date
from helper.database import uploadlimit, usertype, addpre


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["warn"]))
async def warn(c, m):
    if len(m.command) >= 3:
        try:
            user_id = m.text.split(' ', 2)[1]
            reason = m.text.split(' ', 2)[2]
            await m.reply_text("Uᴛɪʟɪsᴀᴛᴇᴜʀ ɴᴏᴛɪғɪᴇ́ ᴀᴠᴇᴄ sᴜᴄᴄᴇ̀s 😁")
            await c.send_message(chat_id=int(user_id), text=reason)
        except:
            await m.reply_text("Uᴛɪʟɪsᴀᴛᴇᴜʀ ɴᴏɴ ɴᴏᴛɪғɪᴇ́ 😔")


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["addpremium"]))
async def buypremium(bot, message):
    await message.reply_text("🦋 Sᴇ́ʟᴇᴄᴛɪᴏɴɴᴇᴢ ᴜɴᴇ ғᴏʀᴍᴜʟᴇ ᴘᴏᴜʀ ᴜᴘɢʀᴀᴅᴇ...", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("🪙 Bᴀsɪᴄ", callback_data="vip1")],
        [InlineKeyboardButton("⚡ Sᴛᴀɴᴅᴀʀᴅ", callback_data="vip2")],
        [InlineKeyboardButton("💎 Pʀᴏ", callback_data="vip3")],
        [InlineKeyboardButton("✖️ Aɴɴᴜʟᴇʀ ✖️", callback_data="cancel")]
    ]))


@Client.on_message((filters.channel | filters.private) & filters.user(OWNER) & filters.command(["ceasepower"]))
async def ceasepremium(bot, message):
    await message.reply_text("😁 Mᴏᴅᴇ ᴅᴇ ʀᴇsᴛʀɪᴄᴛɪᴏɴ ᴀᴄᴛɪᴠᴇ́...", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("Lɪᴍɪᴛᴇ 1GB", callback_data="cp1")],
        [InlineKeyboardButton("Tᴏᴜᴛᴇ ᴘᴏᴜᴠᴏɪʀ ʀᴇᴛɪʀᴇ́ᴇ", callback_data="cp2")],
        [InlineKeyboardButton("✖️ Aɴɴᴜʟᴇʀ ✖️", callback_data="cancel")]
    ]))


@Client.on_message((filters.channel | filters.private) & filters.user(OWNER) & filters.command(["resetpower"]))
async def resetpower(bot, message):
    await message.reply_text(text=f"Vᴏᴜʟᴇᴢ-ᴠᴏᴜs ʀᴇ́ᴇʟʟᴇᴍᴇɴᴛ ʀᴇ́ɴɪᴛɪᴀʟɪsᴇʀ ʟᴇs ʟɪᴍɪᴛᴇs ǫᴜᴏᴛɪᴅɪᴇɴɴᴇs ᴀ̀ 2GB ?", quote=True, reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton("• Oᴜɪ ! Pᴀʀ ᴅᴇ́ғᴀᴜᴛ •", callback_data="dft")],
        [InlineKeyboardButton("❌ Aɴɴᴜʟᴇʀ ❌", callback_data="cancel")]
    ]))


@Client.on_callback_query(filters.regex('vip1'))
async def vip1(bot, update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 21474836500
    uploadlimit(int(user_id), 21474836500)
    usertype(int(user_id), "🪙 Bᴀsɪᴄ")
    addpre(int(user_id))
    await update.message.edit("Aᴊᴏᴜᴛᴇ́ ᴄᴏᴍᴍᴇ ᴜsᴀɢᴇ Pʀᴇᴍɪᴜᴍ ᴄᴀᴘᴀᴄɪᴛᴇ́ 20GB !")
    await bot.send_message(user_id, "Hᴇʏ ! Vᴏᴜs ᴇ̂ᴛᴇs ᴘᴀssᴇ́ ᴀᴜ ᴘʟᴀɴ Bᴀsɪᴄ. Cᴏɴsᴜʟᴛᴇᴢ ᴠᴏᴛʀᴇ ᴘʟᴀɴ /myplan")

@Client.on_callback_query(filters.regex('vip2'))
async def vip2(bot, update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 53687091200
    uploadlimit(int(user_id), 53687091200)
    usertype(int(user_id), "⚡ Sᴛᴀɴᴅᴀʀᴅ")
    addpre(int(user_id))
    await update.message.edit("Aᴊᴏᴜᴛᴇ́ ᴄᴏᴍᴍᴇ ᴜsᴀɢᴇ Pʀᴇᴍɪᴜᴍ ᴄᴀᴘᴀᴄɪᴛᴇ́ 50GB !")
    await bot.send_message(user_id, "Hᴇʏ ! Vᴏᴜs ᴇ̂ᴛᴇs ᴘᴀssᴇ́ ᴀᴜ ᴘʟᴀɴ Sᴛᴀɴᴅᴀʀᴅ. Cᴏɴsᴜʟᴛᴇᴢ ᴠᴏᴛʀᴇ ᴘʟᴀɴ /myplan")


@Client.on_callback_query(filters.regex('vip3'))
async def vip3(bot, update):
    id = update.message.reply_to_message.text.split("/addpremium")
    user_id = id[1].replace(" ", "")
    inlimit = 107374182400
    uploadlimit(int(user_id), 107374182400)
    usertype(int(user_id), "💎 Pʀᴏ")
    addpre(int(user_id))
    await update.message.edit("Aᴊᴏᴜᴛᴇ́ ᴄᴏᴍᴍᴇ ᴜsᴀɢᴇ Pʀᴇᴍɪᴜᴍ ᴄᴀᴘᴀᴄɪᴛᴇ́ 100GB !")
    await bot.send_message(user_id, "Hᴇʏ ! Vᴏᴜs ᴇ̂ᴛᴇs ᴘᴀssᴇ́ ᴀᴜ ᴘʟᴀɴ Pʀᴏ. Cᴏɴsᴜʟᴛᴇᴢ ᴠᴏᴛʀᴇ ᴘʟᴀɴ /myplan")


@Client.on_callback_query(filters.regex('cp1'))
async def cp1(bot, update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 2147483652
    uploadlimit(int(user_id), 2147483652)
    usertype(int(user_id), "⚠️ Cᴏᴍᴘᴛᴇ ᴅᴇ́ɢʀᴀᴅᴇ́")
    addpre(int(user_id))
    await update.message.edit("Rᴇ́ᴅᴜᴄᴛɪᴏɴ ᴅᴇ ᴄᴀᴘᴀᴄɪᴛᴇ́ ᴀ̀ 2GB ᴀᴊᴏᴜᴛᴇ́ᴇ !")
    await bot.send_message(user_id, "Vᴏᴛʀᴇ ᴄᴀᴘᴀᴄɪᴛᴇ́ ᴅ'ᴜᴘʟᴏᴀᴅ ᴀ ᴇ́ᴛᴇ́ ʀᴇ́ᴅᴜɪᴛᴇ ᴀ̀ 2GB. Cᴏɴsᴜʟᴛᴇᴢ ᴠᴏᴛʀᴇ ᴘʟᴀɴ /myplan \n\n**Cᴏɴᴛᴀᴄᴛᴇʀ ʟ'ᴀᴅᴍɪɴ :** @hyoshassistantBot")


@Client.on_callback_query(filters.regex('cp2'))
async def cp2(bot, update):
    id = update.message.reply_to_message.text.split("/ceasepower")
    user_id = id[1].replace(" ", "")
    inlimit = 0
    uploadlimit(int(user_id), 0)
    usertype(int(user_id), "⚠️ Cᴏᴍᴘᴛᴇ ᴅᴇ́ɢʀᴀᴅᴇ́")
    addpre(int(user_id))
    await update.message.edit("Tᴏᴜᴛᴇ ʟᴇ ᴘᴏᴜᴠᴏɪʀ ᴅᴇ ᴄᴇ ᴄᴏᴍᴘᴛᴇ ᴇsᴛ ʀᴇᴛɪʀᴇ́ᴇ !")
    await bot.send_message(user_id, "Vᴏᴛʀᴇ ᴄᴀᴘᴀᴄɪᴛᴇ́ ᴅ'ᴜᴘʟᴏᴀᴅ ᴇsᴛ ᴀᴄᴛᴜᴇʟʟᴇᴍᴇɴᴛ ᴅᴇ 0GB. Cᴏɴsᴜʟᴛᴇᴢ ᴠᴏᴛʀᴇ ᴘʟᴀɴ /myplan \n\n**Cᴏɴᴛᴀᴄᴛᴇʀ ʟ'ᴀᴅᴍɪɴ :** @Hyoshdesign")


@Client.on_callback_query(filters.regex('dft'))
async def dft(bot, update):
    id = update.message.reply_to_message.text.split("/resetpower")
    user_id = id[1].replace(" ", "")
    inlimit = 2147483652
    uploadlimit(int(user_id), 2147483652)
    usertype(int(user_id), "🆓 Gʀᴀᴛᴜɪᴛ")
    addpre(int(user_id))
    await update.message.edit("**Lᴇs ʟɪᴍɪᴛᴇs ǫᴜᴏᴛɪᴅɪᴇɴɴᴇs ᴏɴᴛ ᴇ́ᴛᴇ́ ʀᴇ́ɴɪᴛɪᴀʟɪsᴇ́ᴇs ᴀ̀ 2GB.**")
    await bot.send_message(user_id, "Lɪᴍɪᴛᴇ ǫᴜᴏᴛɪᴅɪᴇɴɴᴇ ʀᴇ́ɴɪᴛɪᴀʟɪsᴇ́ᴇ. Cᴏɴsᴜʟᴛᴇᴢ ᴠᴏᴛʀᴇ ᴘʟᴀɴ /myplan\n\n**Cᴏɴᴛᴀᴄᴛᴇʀ ʟ'ᴀᴅᴍɪɴ :** <a href='https://t.me/Hyoshdesign'>Hyoshdesign</a>")
