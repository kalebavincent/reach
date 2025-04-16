import os
from pyrogram import Client, filters
from config import *
import time
import psutil
from datetime import timedelta

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["log"]))
async def send_log(client, message):
    log_file = "bot.log"
    
    if os.path.exists(log_file):
        await message.reply_document(
            document=log_file,
            caption="ᴠᴏɪᴄɪ ʟᴇ ꜰɪᴄʜɪᴇʀ ᴅᴇ ʟᴏɢ ᴀᴄᴛᴜᴇʟ.",
        )
        
        if len(message.command) > 1 and message.command[1].lower() == "delete":
            os.remove(log_file)
            await message.reply_text("ʟᴇ ꜰɪᴄʜɪᴇʀ ʟᴏɢ ᴀ éᴛé ᴇɴᴠᴏʏé ᴇᴛ ꜱᴜᴘᴘʀɪᴍé.")
    else:
        await message.reply_text("ᴀᴜᴄᴜɴ ꜰɪᴄʜɪᴇʀ ʟᴏɢ ᴛʀᴏᴜᴠé.")

start_time = time.time()
@Client.on_message(filters.command("stats") & filters.user(OWNER))
async def bot_status(client, message):
    try:
        current_time = time.time()
        uptime = str(timedelta(seconds=int(current_time - start_time)))

        cpu_usage = psutil.cpu_percent(interval=1)
        ram_usage = psutil.virtual_memory().percent

        disk_info = psutil.disk_usage('/')
        total_disk_space = convert_size(disk_info.total)
        used_space = convert_size(disk_info.used)
        free_space = convert_size(disk_info.free)

        status_message = f"""
📊 **Bot Status** 📊

⏳ **Uptime**: `{uptime}`
🖥️ **CPU Usage**: `{cpu_usage}%`
📈 **RAM Usage**: `{ram_usage}%`
💾 **Total Disk Space**: `{total_disk_space}`
📂 **Used Space**: `{used_space}`
🗃️ **Free Space**: `{free_space}`
        """
        await message.reply_text(status_message)
    
    except Exception as e:
        await message.reply_text(f"❌ Erreur lors de la récupération des statistiques : `{e}`")


def convert_size(size_bytes):
    if size_bytes == 0:
        return "0B"
    size_name = ("B", "KB", "MB", "GB", "TB")
    i = int((len(bin(size_bytes)) - 2) / 10)
    p = 1024 ** i
    s = round(size_bytes / p, 2)
    return f"{s} {size_name[i]}"