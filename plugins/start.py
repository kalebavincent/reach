from datetime import date as date_ 
import datetime
import os, re
import asyncio
import random
from script import *
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters, enums
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup)
import humanize
from helper.progress import humanbytes
from helper.database import botdata, find_one, total_user
from helper.database import insert, find_one, used_limit, usertype, uploadlimit, addpredata, total_rename, total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import check_expi
from config import *

bot_username = BOT_USERNAME
log_channel = int(LOG_CHANNEL)
token = BOT_TOKEN
botid = token.split(':')[0]

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client, message):
    user_id = message.chat.id
    old = insert(int(user_id))  

    try:
        id = message.text.split(' ')[1]
    except IndexError:
        id = None

    img_folder =IMG_FOLDER
    if os.path.exists(img_folder) and os.listdir(img_folder):
        random_image = random.choice(os.listdir(img_folder))
        random_image_path = os.path.join(img_folder, random_image)
    else:
        random_image_path = None

    loading_sticker_message = await message.reply_sticker("CAACAgIAAxkBAALmzGXSSt3ppnOsSl_spnAP8wHC26jpAAJEGQACCOHZSVKp6_XqghKoHgQ")
    await asyncio.sleep(2)
    await loading_sticker_message.delete()

    txt = f"""Bᴏɴᴊᴏᴜʀ {message.from_user.mention} \n\n➻ Cᴇᴄɪ ɛsᴛ ᴜɴ ʙᴏᴛ ᴀᴠᴀɴᴄé ᴇᴛ ᴘᴏᴡᴇʀғᴜʟ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ.\n\n ➻ ᴜᴛɪʟɪsᴇz ᴄᴇ ʙᴏᴛ ᴘᴏᴜʀ ʀᴇɴᴏᴍᴍᴇʀ ᴇᴛ ᴍᴏᴅɪғɪᴇʀ ʟᴀ ᴠɪɢɴᴇᴛᴛᴇ ᴅᴇ ᴠᴏs ғɪᴄʜɪᴇʀs.\n\n ➻ ᴠᴏᴜs ᴘᴏᴜᴠᴇᴢ ᴇ́ɢᴀʟᴇᴍᴇɴᴛ ᴄᴏɴᴠᴇʀᴛɪʀ ᴜɴᴇ ᴠɪᴅᴇ́ᴏ ᴇɴ ғɪᴄʜɪᴇʀ ᴇᴛ ᴠɪᴄᴇ ᴠᴇʀsᴀ.\n\n➻ ᴄᴇ ʙᴏᴛ ᴘʀᴇɴᴅ ᴇɴ ᴄʜᴀʀɢᴇ ʟᴇs ᴠɪɢɴᴇᴛᴛᴇs ᴇᴛ ʟᴇs ʟᴇ́ɢᴇɴᴅᴇs ᴘᴇʀsᴏɴɴᴀʟɪsᴇ́ᴇs.\n\n<b>ʙᴏᴛ ᴄʀᴇ́ᴇ́ ᴘᴀʀ @hyoshdesign</b>"""

    if random_image_path:
        await message.reply_photo(
            photo=random_image_path,
            caption=txt,
            reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("📢 Mɪsᴇs ᴀ ᴊᴏᴜʀs", url="https://t.me/hyoshdesign"),
                     InlineKeyboardButton("💬 Sᴜᴘᴘᴏʀᴛ", url="https://t.me/hokageclub")],
                    [InlineKeyboardButton("🛠️ ᴀɪᴅᴇ", callback_data='help'),
                     InlineKeyboardButton("❤️‍🩹 ᴀ ᴘʀᴏᴘᴏs", callback_data='about')],
                    [InlineKeyboardButton("🧑‍💻 Dᴇᴠᴇʟᴏᴘᴇᴜʀ 🧑‍💻", url="https://t.me/Hyoshdesign")]
                ]
            )
        )
    else:
        await message.reply(
            text="⚠️ Aucun fichier image trouvé dans le dossier `img`. Veuillez en ajouter.",
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📢 Mɪsᴇs ᴀ ᴊᴏᴜʀs", url="https://t.me/hyoshdesign")]]
            )
        )
    return

@Client.on_message((filters.private & (filters.document | filters.audio | filters.video)) | filters.channel & (filters.document | filters.audio | filters.video))
async def send_doc(client, message):
    update_channel_id = FORCE_SUBS 
    user_id = message.from_user.id
    first_name = message.from_user.first_name 
    last_name = message.from_user.last_name or ""  
    full_name = f"{first_name} {last_name}".strip()

    if update_channel_id:
        try:
            chat = await client.get_chat(update_channel_id)
            update_channel = chat.username 

            await client.get_chat_member(update_channel_id, user_id)
        except UserNotParticipant:
            _newus = find_one(message.from_user.id)
            user = _newus.get("usertype", "Inconnu")

            await message.reply_text(
                f"<b>ʙᴏɴᴊᴏᴜʀ {full_name},\n\n"
                "ᴠᴏᴜꜱ ᴅᴇᴠᴇᴢ ʀᴇᴊᴏɪɴᴅʀᴇ ᴍᴏɴ ᴄᴀɴᴀʟ ᴘᴏᴜʀ ᴍ'ᴜᴛɪʟɪꜱᴇʀ.\n\n"
                "ᴠᴇᴜɪʟʟᴇᴢ ʀᴇᴊᴏɪɴᴅʀᴇ ʟᴇ ᴄᴀɴᴀʟ.</b>",
                reply_to_message_id=message.id,
                reply_markup=InlineKeyboardMarkup(
                    [
                        [InlineKeyboardButton("🔺 Cᴀɴᴀʟ ᴅᴇ ᴍɪsᴇs ᴀ ᴊᴏᴜʀs 1🔺", url=f"https://t.me/{update_channel}")],
                        [InlineKeyboardButton("🔺 Cᴀɴᴀʟ ᴅᴇ ᴍɪsᴇs ᴀ ᴊᴏᴜʀs 2 🔺", url="https://t.me/manga_VF_HD")]
                    ]
                )
            )

            await client.send_message(
                log_channel,
                (
                    f"<b><u>ɴᴏᴜᴠᴇʟ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ ᴀ ᴅéᴍᴀʀʀé ʟᴇ ʙᴏᴛ</u></b>\n\n"
                    f"<b>ɪᴅ ᴅᴇ ʟ'ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ</b> : `{user_id}`\n"
                    f"<b>Pʀéɴᴏᴍ</b> : {first_name}\n"
                    f"<b>ɴᴏᴍ</b> : {last_name or 'ɴᴏɴ ꜱᴘéᴄɪꜰɪé'}\n"
                    f"<b>ɴᴏᴍ ᴅ'ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ</b> : @{message.from_user.username or 'ɴᴏɴ ꜱᴘéᴄɪꜰɪé'}\n"
                    f"<b>ᴍᴇɴᴛɪᴏɴ ᴅᴇ ʟ'ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ</b> : {message.from_user.mention}\n"
                    f"<b>ʟɪᴇɴ ᴅᴇ ʟ'ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ</b> : "
                    f"<a href='tg://openmessage?user_id={user_id}'>ᴄʟɪQᴜᴇᴢ ɪᴄɪ</a>\n"
                    f"<b>ᴘʟᴀɴ ᴅᴇ ʟ'ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ</b> : {user}"
                ),
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("🔺 ʀᴇꜱᴛʀᴇɪɴᴅʀᴇ ʟ'ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ ( **ᴘᴍ** ) 🔺", callback_data="ceasepower")]]
                )
            )
            return

    botdata(int(botid))
    bot_data = find_one(int(botid))
    prrename = bot_data['total_rename']
    prsize = bot_data['total_size']
    user_deta = find_one(user_id)
    used_date = user_deta["date"]
    buy_date = user_deta["prexdate"]
    daily = user_deta["daily"]
    user_type = user_deta["usertype"]

    c_time = time.time()

    if user_type == "Free":
        LIMIT = 120
    else:
        LIMIT = 10
    then = used_date + LIMIT
    left = round(then - c_time)
    conversion = datetime.timedelta(seconds=left)
    ltime = str(conversion)
    if left > 0:
        await message.reply_text(f"<b>Dᴇsᴏʟé, jᴇ n'ᴇxisᴛᴇ pᴀs ᴜɴɪqᴜᴇᴍᴇɴᴛ pᴏᴜʀ vᴏᴜs.\n\nLᴇ cᴏɴtrᴏʟᴇ ᴅᴇ sᴀᴛᴜʀᴀᴛɪᴏɴ ɛst ᴀᴄᴛɪғ.\nVᴇᴜɪʟʟᴇᴢ ᴀᴛᴛᴇɴᴅʀᴇ {ltime}. \n ᴏᴜ ᴘᴀꜱꜱᴇᴇʀ ᴀᴜ ᴘʟᴀɴ ꜱᴜᴘᴘᴇʀɪᴇᴜʀ  \n /upgrade</b>", reply_to_message_id=message.id)
    else:
        # Forward a single message
        media = await client.get_messages(message.chat.id, message.id)
        file = media.document or media.video or media.audio
        dcid = FileId.decode(file.file_id).dc_id
        filename = file.file_name
        file_id = file.file_id
        value = 2147483648
        used_ = find_one(message.from_user.id)
        used = used_["used_limit"]
        limit = used_["uploadlimit"]
        expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
        if expi != 0:
            today = date_.today()
            pattern = '%Y-%m-%d'
            epcho = int(time.mktime(time.strptime(str(today), pattern)))
            daily_(message.from_user.id, epcho)
            used_limit(message.from_user.id, 0)
        remain = limit - used
        if remain < int(file.file_size):
            await message.reply_text(f"100% ᴅᴇ vᴏᴛʀᴇ qᴜᴏᴛᴀ ǫᴜᴏᴛɪᴇɴ ᴅᴇ {humanbytes(limit)} ᴅᴇ ᴅᴀᴛᴀs ᴇst épᴜɪsé.\n\n<b> ᴛᴀɪʟʟᴇ ᴅᴜ ғɪʟᴇ ᴅéᴛᴇᴄᴛéᴇ :</b> {humanbytes(file.file_size)}\n<b>Qᴜᴏᴛᴀ ǫᴜᴏᴛɪᴇɴ ᴜsᴀɢé :</b> {humanbytes(used)}\n\nIl vous reste uniquement <b>{humanbytes(remain)}</b> sur votre compte.\n\nSɪ vᴏᴜs sᴏʜᴀɪᴛᴇz ʀᴇɴᴏᴍᴍᴇʀ ᴅᴇs ɢʀᴏs ғɪʟᴇs, ᴍᴇᴛᴛᴇz ᴀ ᴊᴏᴜʀ ᴠᴏᴛʀᴇ ᴘʟᴀɴ", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Mᴇᴛᴛᴇʀ ᴀ ᴊᴏᴜʀ", callback_data="my_pl_call")]]))
            return
        if value < file.file_size:
            if STRING:
                if buy_date == None:
                    await message.reply_text(f"Vᴏᴜs nᴇ pᴏᴜᴠᴇz pᴀs ᴅᴏᴜʙʟᴇʀ ᴜɴ ғɪʟᴇ ᴅᴇ pʟᴜs ᴅᴇ 2 ɢᴏ\n\nVᴏᴛʀᴇ pʟᴀɴ nᴇ pᴇʀᴍᴇᴛ ᴘᴀs ᴅᴏᴜʙʟᴇʀ ᴅᴇs ɢᴏs 2 ɢᴏ\n\nMᴇᴛᴛᴇz ᴀ ᴊᴏᴜʀ vᴏᴛʀᴇ ᴘʟᴀɴ pᴏᴜʀ ʀᴇɴᴏᴍᴍᴇʀ ᴅᴇs ɢʀᴏs ɢᴏs", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💳 Mᴇᴛᴛᴇʀ ᴀ ᴊᴏᴜʀ", callback_data="my_pl_call")]]))
                    return
                pre_check = check_expi(buy_date)
                if pre_check == True:
                    await message.reply_text(f"""__Qᴜᴇ sʜouaiᴛᴇᴢ-ᴠᴏᴜs faire avec ce fichier?__\n\n**Nᴏᴍ ᴅᴜ ғɪʟᴇ** :- `{filename}`\n**Tᴀɪʟʟᴇ ᴅᴜ ғɪʟᴇ** :- {humanize.naturalsize(file.file_size)}\n**ID DC** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("📝 Rᴇɴᴏᴍᴍᴇʀ", callback_data="rename"), InlineKeyboardButton("✖️ Aɴɴᴜʟᴇʀ", callback_data="cancel")]]))
                    total_rename(int(botid), prrename)
                    total_size(int(botid), prsize, file.file_size)
                else:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")
                    await message.reply_text(f'Vᴏᴛʀᴇ pʟᴀɴ ᴀ ᴇxpɪʀé lᴇ {buy_date}', quote=True)
                    return
            else:
                await message.reply_text("Vᴏᴜs nᴇ pᴏᴜᴠᴇz pᴀs ᴅᴏᴜʙʟᴇʀ ᴜɴ ғɪʟᴇ ᴅᴇ pʟᴜs ᴅᴇ 2 ɢᴏ\n\nVᴏᴛʀᴇ pʟᴀɴ nᴇ pᴇʀᴍᴇᴛ ᴘᴀs ᴅᴏᴜʙʟᴇʀ ᴅᴇs ɢᴏs 2 ɢᴏ\n\nMᴇᴛᴛᴇz ᴀ ᴊᴏᴜʀ vᴏᴛʀᴇ ᴘʟᴀɴ pᴏᴜʀ ʀᴇɴᴏᴍᴍᴇʀ ᴅᴇs ɢᴏs 2 ɢᴏ")
                return
        else:
            if buy_date:
                pre_check = check_expi(buy_date)
                if pre_check == False:
                    uploadlimit(message.from_user.id, 2147483648)
                    usertype(message.from_user.id, "Free")
            
            filesize = humanize.naturalsize(file.file_size)
            fileid = file.file_id
            total_rename(int(botid), prrename)
            total_size(int(botid), prsize, file.file_size)
            await message.reply_text(f"""__Qᴜᴇ ꜱʜᴏᴜᴀɪᴛᴇᴢ-ᴠᴏᴜꜱ ꜰᴀɪʀᴇ ᴀᴠᴇᴄ ᴄᴇ ꜰɪᴄʜɪᴇʀ?__\n\n**Nᴏᴍ ᴅᴜ ғɪʟᴇ** :- `{filename}`\n**Tᴀɪʟʟᴇ ᴅᴜ ғɪʟᴇ** :- {filesize}\n**ID DC** :- {dcid}""", reply_to_message_id=message.id, reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("📝 Rᴇɴᴏᴍᴍᴇʀ", callback_data="rename"),
                  InlineKeyboardButton("✖️ Aɴɴᴜʟᴇʀ", callback_data="cancel")]]))
