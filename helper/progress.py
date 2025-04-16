import math
import time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

async def progress_for_pyrogram(current, total, ud_type, message, start):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress_bar_length = 8  
        completed_length = math.floor(percentage / (100 / progress_bar_length))
        progress_bar = ''.join(["█" for _ in range(completed_length)]) + \
                       ''.join(["░" for _ in range(progress_bar_length - completed_length)])

        progress = f"📊 **ᴘʀᴏɢʀᴇꜱꜱ**: [{progress_bar}] **{round(percentage, 2)}%**\n"
        details = (
            f"📥 **ᴅᴏᴡɴʟᴏᴀᴅᴇᴅ**: `{humanbytes(current)}` **ꜱᴜʀ** `{humanbytes(total)}`\n"
            f"⚡ **ꜱᴘᴇᴇᴅ**: `{humanbytes(speed)}/s`\n"
            f"⏳ **ᴇᴛᴀ**: `{estimated_total_time if estimated_total_time else '0 s'}`\n"
            f"🕒 **ᴇʟᴀᴘꜱᴇᴅ ᴛɪᴍᴇ**: `{elapsed_time}`"
        )

        # Cancel button
        cancel_button = InlineKeyboardButton("✖️ ᴄᴀɴᴄᴇʟ ✖️", callback_data="cancel")

        try:
            await message.edit(
                text=f"{ud_type}\n\n{progress}{details}",
                reply_markup=InlineKeyboardMarkup([[cancel_button]])
            )
        except Exception:
            pass


def humanbytes(size):
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'Ki', 2: 'Mi', 3: 'Gi', 4: 'Ti'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
