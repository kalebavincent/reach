from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from pyrogram import Client, filters
from script import *
from config import *


@Client.on_callback_query(filters.regex('about'))
async def about(bot, update):
    text = script.ABOUT_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 ʀᴇᴛᴏᴜʀ", callback_data="home")]
    ])
    await update.message.edit(text=text, reply_markup=keybord)


@Client.on_message(filters.private & filters.command(["donate"]))
async def donatecm(bot, message):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🦋 ᴀᴅᴍɪɴ", url="https://t.me/Hyoshdesign"),
         InlineKeyboardButton("✖️ ғᴇʀᴍᴇʀ", callback_data="cancel")]
    ])
    await message.reply_text(text=text, reply_markup=keybord)


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["admin"]))
async def admincm(bot, message):
    text = script.ADMIN_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("✖️ ғᴇʀᴍᴇʀ ✖️", callback_data="cancel")]
    ])
    await message.reply_text(text=text, reply_markup=keybord)


@Client.on_callback_query(filters.regex('help'))
async def help(bot, update):
    text = script.HELP_TXT.format(update.from_user.mention)
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton('🏞 ᴠɪɢɴᴇᴛᴛᴇ', callback_data='thumbnail'),
         InlineKeyboardButton('✏ ʟᴇ́ɢᴇɴᴅᴇ', callback_data='caption')],
        [InlineKeyboardButton('🏠 ᴀᴄᴄᴜᴇɪʟ', callback_data='home'),
         InlineKeyboardButton('💵 ғᴀɪʀᴇ ᴜɴ ᴅᴏɴ', callback_data='donate')]
    ])

    if update.message.text != text:
        await update.message.edit(text=text, reply_markup=keybord)
    else:
        print("Le texte est déjà identique, aucune modification effectuée.")


@Client.on_callback_query(filters.regex('thumbnail'))
async def thumbnail(bot, update):
    text = script.THUMBNAIL_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 ʀᴇᴛᴏᴜʀ", callback_data="help")]
    ])
    await update.message.edit(text=text, reply_markup=keybord)


@Client.on_callback_query(filters.regex('caption'))
async def caption(bot, update):
    text = script.CAPTION_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 ʀᴇᴛᴏᴜʀ", callback_data="help")]
    ])
    await update.message.edit(text=text, reply_markup=keybord)


@Client.on_callback_query(filters.regex('donate'))
async def donate(bot, update):
    text = script.DONATE_TXT
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("🔙 ʀᴇᴛᴏᴜʀ", callback_data="help")]
    ])
    await update.message.edit(text=text, reply_markup=keybord)


@Client.on_callback_query(filters.regex('home'))
async def home_callback_handler(bot, query):
    text = f"""ʜᴇʟʟᴏ {query.from_user.mention} 🌟

    ➻ ᴄᴇᴄɪ ᴇsᴛ ᴜɴ ʙᴏᴛ ᴘᴜɪssᴀɴᴛ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ.

    ➻ ᴜᴛɪʟɪsᴇz ᴄᴇ ʙᴏᴛ ᴘᴏᴜʀ ʀᴇɴᴏᴍᴍᴇʀ ᴇᴛ ᴍᴏᴅɪғɪᴇʀ ʟᴀ ᴠɪɢɴᴇᴛᴛᴇ ᴅᴇ ᴠᴏs ғɪᴄʜɪᴇʀs.

    ➻ ᴠᴏᴜs ᴘᴏᴜᴠᴇᴢ ᴇ́ɢᴀʟᴇᴍᴇɴᴛ ᴄᴏɴᴠᴇʀᴛɪʀ ᴜɴᴇ ᴠɪᴅᴇ́ᴏ ᴇɴ ғɪᴄʜɪᴇʀ ᴇᴛ ᴠɪᴄᴇ ᴠᴇʀsᴀ.

    ➻ ᴄᴇ ʙᴏᴛ ᴘʀᴇɴᴅ ᴇɴ ᴄʜᴀʀɢᴇ ʟᴇs ᴠɪɢɴᴇᴛᴛᴇs ᴇᴛ ʟᴇs ʟᴇ́ɢᴇɴᴅᴇs ᴘᴇʀsᴏɴɴᴀʟɪsᴇ́ᴇs.

    <b>ʙᴏᴛ ᴄʀᴇ́ᴇ́ ᴘᴀʀ @hyoshdesign</b>"""
    keybord = InlineKeyboardMarkup([
        [InlineKeyboardButton("📢 ᴀᴄᴛᴜᴀʟɪᴛᴇ́s", url="https://t.me/hyoshdesign"),
         InlineKeyboardButton("💬 sᴜᴘᴘᴏʀᴛ", url="https://t.me/hokageclub")],
        [InlineKeyboardButton("🛠️ ᴀɪᴅᴇ", callback_data='help'),
         InlineKeyboardButton("❤️‍🩹 ᴀ̀ ᴘʀᴏᴘᴏs", callback_data='about')],
        [InlineKeyboardButton("🧑‍💻 ᴅᴇ́ᴠᴇʟᴏᴘᴘᴇᴜʀ 🧑‍💻", url="https://t.me/Hyoshdesign")]
    ])
    await query.message.edit_text(text=text, reply_markup=keybord)
