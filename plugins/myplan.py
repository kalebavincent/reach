import time
from pyrogram import Client, filters
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
from helper.database import find_one, used_limit
from helper.database import daily as daily_
import datetime
from datetime import datetime
from datetime import date as date_
from helper.progress import humanbytes
from helper.database import daily as daily_
from helper.date import check_expi
from helper.database import uploadlimit, usertype


@Client.on_message(filters.private & filters.command(["myplan"]))
async def start(client, message):
    used_ = find_one(message.from_user.id)
    daily = used_["daily"]
    expi = daily - \
        int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
    if expi != 0:
        today = date_.today()
        pattern = '%Y-%m-%d'
        epcho = int(time.mktime(time.strptime(str(today), pattern)))
        daily_(message.from_user.id, epcho)
        used_limit(message.from_user.id, 0)
    _newus = find_one(message.from_user.id)
    used = _newus["used_limit"]
    limit = _newus["uploadlimit"]
    remain = int(limit) - int(used)
    user = _newus["usertype"]
    ends = _newus["prexdate"]
    if ends:
        pre_check = check_expi(ends)
        if pre_check == False:
            uploadlimit(message.from_user.id, 2147483652)
            usertype(message.from_user.id, "Free")
    if ends == None:
        text = f"**ᴜᴛɪʟɪsᴀᴛᴇᴜʀ ɪᴅ :** `{message.from_user.id}` \n**ɴᴏᴍ :** {message.from_user.mention} \n\n**🏷 ᴘʟᴀɴ :** {user} \n\n✓ ᴄʜᴀʀɢᴇᴍᴇɴᴛ ᴅᴇ ғɪᴄʜɪᴇʀs ᴊᴜsǫᴜ'ᴀ̀ 2 ɢᴏ \n✓ ᴄᴏᴛᴀ ǫᴜᴏᴛɪᴅɪᴇɴɴᴇ : {humanbytes(limit)} \n✓ ᴜᴛɪʟɪsᴀᴛɪᴏɴ ᴅᴜ ᴊᴏᴜʀ : {humanbytes(used)} \n✓ ʀᴇsᴛᴀɴᴛ : {humanbytes(remain)} \n✓ ᴛɪᴍᴇᴏᴜᴛ : 2 ᴍɪɴᴜᴛᴇs \n✓ ᴘʀᴏᴄᴇssᴜs ᴘᴀʀᴀʟʟᴇ̀ʟᴇs : ɪʟʟɪᴍɪᴛᴇ́ \n✓ ᴇsᴘᴀᴄᴇ ᴛᴇᴍᴘᴏʀᴇʟ : ᴏᴜɪ \n\n**ᴠᴀʟɪᴅɪᴛᴇ́ :** À ᴠɪᴇ"
    else:
        normal_date = datetime.fromtimestamp(ends).strftime('%Y-%m-%d')
        text = f"**ᴜᴛɪʟɪsᴀᴛᴇᴜʀ ɪᴅ :** `{message.from_user.id}` \n**ɴᴏᴍ :** {message.from_user.mention} \n\n**🏷 ᴘʟᴀɴ :** {user} \n\n✓ ᴘʀɪᴏʀɪᴛᴇ́ ᴇ́ʟᴇᴠᴇ́ᴇ \n✓ ᴄʜᴀʀɢᴇᴍᴇɴᴛ ᴅᴇ ғɪᴄʜɪᴇʀs ᴊᴜsǫᴜ'ᴀ̀ 4 ɢᴏ \n✓ ᴄᴏᴛᴀ ǫᴜᴏᴛɪᴅɪᴇɴɴᴇ : {humanbytes(limit)} \n✓ ᴜᴛɪʟɪsᴀᴛɪᴏɴ ᴅᴜ ᴊᴏᴜʀ : {humanbytes(used)} \n✓ ʀᴇsᴛᴀɴᴛ : {humanbytes(remain)} \n✓ ᴛɪᴍᴇᴏᴜᴛ : 0 sᴇᴄᴏɴᴅᴇs \n✓ ᴘʀᴏᴄᴇssᴜs ᴘᴀʀᴀʟʟᴇ̀ʟᴇs : ɪʟʟɪᴍɪᴛᴇ́ \n✓ ᴇsᴘᴀᴄᴇ ᴛᴇᴍᴘᴏʀᴇʟ : ᴏᴜɪ \n\n**ᴠᴏᴛʀᴇ ᴘʟᴀɴ s'ᴇɴᴅʀᴀ ʟᴇ :** {normal_date}"

    if user == "Free":
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 ᴍᴇᴛᴛʀᴇ à ᴊᴏᴜʀ", callback_data="upgrade"), InlineKeyboardButton("✖️ ᴀɴɴᴜʟᴇʀ", callback_data="cancel")]]))
    else:
        await message.reply(text, quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("✖️ ᴀɴɴᴜʟᴇʀ ✖️", callback_data="cancel")]]))
