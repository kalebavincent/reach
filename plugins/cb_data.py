from helper.progress import progress_for_pyrogram
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ForceReply
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from helper.database import *
import os
import random
from PIL import Image
import time
from datetime import date as date_
from datetime import timedelta, datetime
from helper.ffmpeg import take_screen_shot, fix_thumb
from helper.progress import humanbytes
from helper.set import escape_invalid_curly_brackets
import config
from config import *
from pathlib import Path
import logging
from helper.font import FontConverter

log_channel=int(LOG_CHANNEL)

app = Client("client", api_id=API_ID, api_hash=API_HASH)

@Client.on_callback_query(filters.regex('cancel'))
async def cancel(bot, update):
    try:
        await update.message.delete()
    except:
        return

@Client.on_callback_query(filters.regex('rename'))
async def rename(bot, update):
    date_fa = str(update.message.date)
    pattern = '%Y-%m-%d %H:%M:%S'
    date = int(time.mktime(time.strptime(date_fa, pattern)))
    chat_id = update.message.chat.id
    id = update.message.reply_to_message_id
    await update.message.delete()
    await update.message.reply_text(
        f"__ᴠᴇᴜɪʟʟᴇᴢ ᴇɴᴛʀᴇʀ ʟᴇ ɴᴏᴜᴠᴇᴀᴜ ɴᴏᴍ ᴅᴇ ꜰɪᴄʜɪᴇʀ...__\n\nNote:- ʟ'ᴇxᴛᴇɴꜱɪᴏɴ ɴ'ᴇꜱᴛ ᴘᴀꜱ ʀᴇQᴜɪꜱᴇ",
        reply_to_message_id=id,
        reply_markup=ForceReply(True)
    )
    dateupdate(chat_id, date)


@Client.on_callback_query(filters.regex("doc"))
async def doc(bot, update):
    new_name = update.message.text
    used_ = find_one(update.from_user.id)
    used = used_["used_limit"]
    date = used_["date"]
    name = new_name.split(":-")
    new_filename = name[1]
    file_path = os.path.join("downloads", new_filename)  
    message = update.message.reply_to_message
    file = message.document or message.video or message.audio
    ms = await update.message.edit("ᴛᴇɴᴛᴀᴛɪᴠᴇ ᴅᴇ ᴛéʟéᴄʜᴀʀɢᴇᴍᴇɴᴛ...")

    # Mise à jour des limites d'utilisation
    used_limit(update.from_user.id, file.file_size)
    c_time = time.time()
    total_used = used + int(file.file_size)
    used_limit(update.from_user.id, total_used)

    try:
        # Téléchargement du fichier
        path = await bot.download_media(
            message=file,
            progress=progress_for_pyrogram,
            progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴄʜᴀʀɢᴇᴍᴇɴᴛ...", ms, c_time)
        )
    except Exception as e:
        neg_used = used - int(file.file_size)
        used_limit(update.from_user.id, neg_used)
        await ms.edit(e)
        return

    # Renommage du fichier téléchargé
    splitpath = path.split(os.path.sep + "downloads" + os.path.sep)
    dow_file_name = splitpath[1]
    old_file_name = os.path.join("downloads", dow_file_name)
    os.rename(old_file_name, file_path)
    
    user_id = int(update.message.chat.id)
    data = find(user_id)

    try:
        c_caption = data[1]
    except:
        pass

    thumb = data[0]
    watermark_font = find(int(user_id))[2]
    if c_caption:
        doc_list = ["filename", "filesize"]
        new_tex = escape_invalid_curly_brackets(c_caption, doc_list)
        caption = f"**{new_tex.format(filename=new_filename, filesize=humanbytes(file.file_size))}**"
    else:
        caption = f"**{new_filename}**"

    if watermark_font:
        caption = FontConverter(caption).convert(caption, watermark_font)

    if thumb:
        ph_path = await bot.download_media(thumb)
        Image.open(ph_path).convert("RGB").save(ph_path)
        img = Image.open(ph_path)
        img.resize((320, 320))
        img.save(ph_path, "JPEG")
        c_time = time.time()
    else:
        ph_path = None

    value = 2090000000
    if value < file.file_size:
        await ms.edit("ᴛᴇɴᴛᴀᴛɪᴠᴇ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇᴍᴇɴᴛ...")
        try:
            filw = await app.send_document(
                log_channel,
                document=file_path,
                thumb=ph_path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...", ms, c_time)
            )
            from_chat = filw.chat.id
            mg_id = filw.id
            time.sleep(2)
            await bot.copy_message(update.from_user.id, from_chat, mg_id)
            await ms.delete()
            os.remove(file_path)
            try:
                os.remove(ph_path)
            except:
                pass
        except Exception as e:
            neg_used = used - int(file.file_size)
            used_limit(update.from_user.id, neg_used)
            await ms.edit(e)
            os.remove(file_path)
            try:
                os.remove(ph_path)
            except:
                pass
    else:
        await ms.edit("ᴛᴇɴᴛᴀᴛɪᴠᴇ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇᴍᴇɴᴛ...")
        c_time = time.time()
        try:
            await bot.send_document(
                update.from_user.id,
                document=file_path,
                thumb=ph_path,
                caption=caption,
                progress=progress_for_pyrogram,
                progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...", ms, c_time)
            )
            await ms.delete()
            os.remove(file_path)
        except Exception as e:
            neg_used = used - int(file.file_size)
            used_limit(update.from_user.id, neg_used)
            await ms.edit(e)
            os.remove(file_path)
            return


@Client.on_callback_query(filters.regex("vid"))
async def vid(bot, update):
    try:
        new_name = update.message.text
        used_data = find_one(update.from_user.id)
        used = used_data["used_limit"]

        name = new_name.split(":-")
        if len(name) < 2:
            await update.message.edit("Invalid name format.")
            return
        new_filename = name[1]

        file_path = os.path.join("downloads", new_filename)

        message = update.message.reply_to_message
        file = message.document or message.video or message.audio

        ms = await update.message.edit("ᴛᴇɴᴛᴀᴛɪᴠᴇ ᴅᴇ ᴛéʟéᴄʜᴀʀɢᴇᴍᴇɴᴛ...")
        used_limit(update.from_user.id, file.file_size)
        c_time = time.time()
        total_used = used + int(file.file_size)
        used_limit(update.from_user.id, total_used)

        path = await bot.download_media(
            message=file,
            progress=progress_for_pyrogram,
            progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴄʜᴀʀɢᴇᴍᴇɴᴛ...", ms, c_time)
        )

        splitpath = path.split(os.path.sep + "downloads" + os.path.sep)
        if len(splitpath) < 2:
            await ms.edit("Error: Couldn't split the downloaded path.")
            return
        dow_file_name = splitpath[1]
        old_file_name = os.path.join("downloads", dow_file_name)

        os.rename(old_file_name, file_path)

        user_id = int(update.message.chat.id)
        data = find(user_id)

        try:
            c_caption = data[1]
        except:
            c_caption = None

        thumb = data[0]
        watermark_font = find(int(user_id))[2]

        duration = 0
        metadata = extractMetadata(createParser(file_path))

        if metadata.has("duration"):
            duration = metadata.get('duration').seconds

        width, height = 320, 180  # Default dimensions for landscape (16:9)

        if metadata.has("width") and metadata.has("height"):
            original_width = metadata.get("width")
            original_height = metadata.get("height")

            # Force landscape (16:9)
            if original_width / original_height != 16 / 9:
                height = 180
                width = int(height * 16 / 9)
            else:
                width = original_width
                height = original_height

        if c_caption:
            vid_list = ["filename", "filesize", "duration"]
            new_tex = escape_invalid_curly_brackets(c_caption, vid_list)
            caption = f"**{new_tex.format(filename=new_filename, filesize=humanbytes(file.file_size), duration=timedelta(seconds=duration))}**"
        else:
            caption = f"**{new_filename}**"

        if thumb:
            ph_path = await bot.download_media(thumb)
        else:
            try:
                ph_path_ = await take_screen_shot(
                    file_path, os.path.dirname(os.path.abspath(file_path)),
                    random.randint(0, duration - 1)
                )
                _, _, ph_path = await fix_thumb(ph_path_)
            except Exception as e:
                ph_path =DEFAUTTHUMB

        # Resize thumbnail to 16:9
        if ph_path:
            img = Image.open(ph_path)
            img_width, img_height = img.size

            if img_width / img_height != 16 / 9:
                new_height = 180
                new_width = int(new_height * 16 / 9)
                img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
                img.save(ph_path, "JPEG", quality=95)
        
        if watermark_font:
            caption = FontConverter(caption).convert(caption, watermark_font)

        value = 2090000000
        if value < file.file_size:
            await ms.edit("ᴛᴇɴᴛᴀᴛɪᴠᴇ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇᴍᴇɴᴛ...")
            try:
                filw = await bot.send_video(
                    log_channel,
                    video=file_path,
                    thumb=ph_path,
                    duration=duration,
                    width=width,
                    height=height,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...", ms, c_time)
                )

                from_chat = filw.chat.id
                mg_id = filw.id
                time.sleep(2)
                await bot.copy_message(update.from_user.id, from_chat, mg_id)
                await ms.delete()
                os.remove(file_path)
                if ph_path:
                    os.remove(ph_path)
            except Exception as e:
                used_limit(update.from_user.id, used - int(file.file_size))
                await ms.edit(f"Error: {e}")
                os.remove(file_path)
                if ph_path:
                    os.remove(ph_path)
        else:
            await ms.edit("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...")
            c_time = time.time()
            try:
                await bot.send_video(
                    update.from_user.id,
                    video=file_path,
                    thumb=ph_path,
                    duration=duration,
                    width=width,
                    height=height,
                    caption=caption,
                    progress=progress_for_pyrogram,
                    progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...", ms, c_time)
                )
                await ms.delete()
                os.remove(file_path)
                if ph_path:
                    os.remove(ph_path)
            except Exception as e:
                used_limit(update.from_user.id, used - int(file.file_size))
                await ms.edit(f"Error: {e}")
                os.remove(file_path)

    except Exception as e:
        await update.message.edit(f"An error occurred: {e}")

@Client.on_callback_query(filters.regex("aud"))
async def aud(bot, update):
    new_name = update.message.text
    used_ = find_one(update.from_user.id)
    used = used_["used_limit"]

    name = new_name.split(":-")
    new_filename = name[1]
    file_path = os.path.join("downloads", new_filename) 
    message = update.message.reply_to_message
    file = message.document or message.video or message.audio

    total_used = used + int(file.file_size)
    used_limit(update.from_user.id, total_used)
    ms = await update.message.edit("ᴛᴇɴᴛᴀᴛɪᴠᴇ ᴅᴇ ᴛéʟéᴄʜᴀʀɢᴇᴍᴇɴᴛ...")
    c_time = time.time()

    try:
        path = await bot.download_media(
            message=file,
            progress=progress_for_pyrogram,
            progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴄʜᴀʀɢᴇᴍᴇɴᴛ...", ms, c_time)
        )
    except Exception as e:
        neg_used = used - int(file.file_size)
        used_limit(update.from_user.id, neg_used)
        await ms.edit(str(e))
        return

    dow_file_name = os.path.basename(path)
    old_file_name = os.path.join("downloads", dow_file_name)
    os.rename(old_file_name, file_path)

    duration = 0
    metadata = extractMetadata(createParser(file_path))
    if metadata and metadata.has("duration"):
        duration = metadata.get('duration').seconds

    user_id = int(update.message.chat.id)
    data = find(user_id)
    c_caption = data[1] if len(data) > 1 else None
    thumb = data[0]
    watermark_font = find(int(user_id))[2]

    if c_caption:
        aud_list = ["filename", "filesize", "duration"]
        new_tex = escape_invalid_curly_brackets(c_caption, aud_list)
        caption = new_tex.format(
            filename=new_filename,
            filesize=humanbytes(file.file_size),
            duration=timedelta(seconds=duration)
        )
    else:
        caption = f"**{new_filename}**"
        
    if watermark_font:
        caption = FontConverter(caption).convert(caption, watermark_font)

    ph_path = None
    if thumb:
        ph_path = await bot.download_media(thumb)
        Image.open(ph_path).convert("RGB").save(ph_path)
        img = Image.open(ph_path)
        img.resize((320, 320)).save(ph_path, "JPEG")

    await ms.edit("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...")
    c_time = time.time()

    try:
        await bot.send_audio(
            update.message.chat.id,
            audio=file_path,
            caption=caption,
            thumb=ph_path,
            duration=duration,
            progress=progress_for_pyrogram,
            progress_args=("ᴇɴ ᴛʀᴀɪɴ ᴅᴇ ᴛéʟéᴠᴇʀꜱᴇʀ...", ms, c_time)
        )
        await ms.delete()
    except Exception as e:
        neg_used = used - int(file.file_size)
        used_limit(update.from_user.id, neg_used)
        await ms.edit(str(e))
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)
        if ph_path and os.path.exists(ph_path):
            os.remove(ph_path)



