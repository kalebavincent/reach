from pyrogram.errors import FloodWait
import asyncio
from pyrogram import Client, filters
from helper.database import getid, delete
from config import *

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["broadcast"]))
async def broadcast(bot, message):
    if message.reply_to_message:
        ms = await message.reply_text("ʀᴇᴄᴜᴘᴇʀᴀᴛɪᴏɴ ᴅᴇ ᴛᴏᴜᴛᴇs ʟᴇs ɪᴅs ᴅᴀɴs ʟᴀ ʙᴀsᴇ ᴅᴇ ᴅᴏɴɴᴇᴇs...\nᴘᴀᴛɪᴇɴᴛᴇᴢ.")
        ids = getid()
        total_ids = len(ids)
        success = 0
        failed = 0
        
        await ms.edit(f"ᴅᴇ́ᴍᴀʀʀᴀɢᴇ ᴅᴜ ʙʀᴏᴀᴅᴄᴀsᴛ...\nᴇɴᴠᴏɪ ᴅᴇ ᴍᴇssᴀɢᴇs ᴀ̀ {total_ids} ᴜᴛɪʟɪsᴀᴛᴇᴜʀs.")

        for user_id in ids:
            try:
                await message.reply_to_message.copy(user_id)
                success += 1
            except FloodWait as e:
                await asyncio.sleep(e.value)
            except Exception as e:
                failed += 1
                delete({"_id": user_id})
            
            if (success + failed) % 10 == 0 or (success + failed) == total_ids:
                try:
                    await ms.edit(
                        f"ᴍᴇssᴀɢᴇ ᴇɴᴠᴏʏᴇ́ ᴀ̀ {success} ᴜᴛɪʟɪsᴀᴛᴇᴜʀs.\n"
                        f"ᴇ́ᴄʜᴇᴄ ᴅᴇ ʟ'ᴇɴᴠᴏɪ ᴘᴏᴜʀ {failed} ᴜᴛɪʟɪsᴀᴛᴇᴜʀs.\n"
                        f"ᴛᴏᴛᴀʟ : {total_ids}."
                    )
                except Exception:
                    pass

        await ms.edit(
            f"ʙʀᴏᴀᴅᴄᴀsᴛ ᴛᴇʀᴍɪɴᴇ́ !\n\n"
            f"✅ ᴇɴᴠᴏʏᴇ́ ᴀ̀ {success} ᴜᴛɪʟɪsᴀᴛᴇᴜʀs.\n"
            f"❌ ᴇ́ᴄʜᴇᴄ ᴘᴏᴜʀ {failed} ᴜᴛɪʟɪsᴀᴛᴇᴜʀs.\n"
            f"📊 ᴛᴏᴛᴀʟ : {total_ids}."
        )
