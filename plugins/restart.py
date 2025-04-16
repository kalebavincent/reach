# import os, sys, asyncio
# from config import *
# from pyrogram import filters, Client

# @Client.on_message(filters.command("restart") & filters.user(OWNER))
# async def stop_button(bot, message):
#     msg = await bot.send_message(text="🔄 ᴘʀᴏᴄᴇssᴜs ᴀɴɴᴜʟᴇʀ. ʙᴏᴛ ᴇᴛ ᴇɴ ʀᴇsᴛᴀʀᴛ....", chat_id=message.chat.id)       
#     await asyncio.sleep(3)
#     await msg.edit("✅️ ʙᴏᴛ ᴇsᴛ ʀᴇsᴛᴀʀᴛᴇ. ᴍᴀɴᴛᴇɴᴀɴᴛ ᴠᴏᴜs ᴘᴏᴜᴠᴇᴢ ᴍᴇ ᴜsᴇʀ")
#     os.execl(sys.executable, sys.executable, *sys.argv)




from pyrogram import filters, Client
import sys
from config import *

@Client.on_message(filters.command("restart") & filters.user(OWNER))
async def stop_button(bot, message):
    await bot.send_message(
        chat_id=message.chat.id,
        text="🔄 ʟᴇ ʙᴏᴛ ʀᴇᴅéᴍᴀʀʀᴇ... ᴠᴇᴜɪʟʟᴇᴢ ᴘᴀᴛɪᴇɴᴛᴇʀ QᴜᴇʟQᴜᴇꜱ ꜱᴇᴄᴏɴᴅᴇꜱ."
    )
    sys.exit(0)  
