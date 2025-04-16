class mr(object):
    PROGRESS_BAR = """\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣⪼ 🗂️ : {1} | {2}
┣⪼ ⏳️ : {0}%
┣⪼ 🚀 : {3}/s
┣⪼ ⏱️ : {4}
╰━━━━━━━━━━━━━━━➣ """

    ABOUT_TXT = """
╭───────────⍟
├🤖 ᴍʏ ɴᴀᴍᴇ : {}
├👑 ᴅᴇᴠᴇʟᴏᴘᴇʀs : <a href=https://t.me/hyoshdesign>@hyoshdesign</a> 
├👨‍💻 ᴘʀᴏɢʀᴀᴍᴇʀ : <a href=https://github.com/oVo-hyoshdesign>hyoshdesign</a>
├📕 ʟɪʙʀᴀʀʏ : <a href=https://github.com/pyrogram>Pyrogram</a>
├✏️ ʟᴀɴɢᴜᴀɢᴇ : <a href=https://www.python.org>Python 3</a>
├💾 ᴅᴀᴛᴀ ʙᴀsᴇ : <a href=https://cloud.mongodb.com>MongoDB</a>
├🌀 ᴍʏ sᴇʀᴠᴇʀ : <a href=https://dashboard.render.com>Render</a>
├📊 ʙᴜɪʟᴅ sᴛᴀᴛᴜs : v3.6.8 [ ᴍᴀᴊᴏʀ ]              
╰───────────────⍟
                                """
    HELP_TXT = """
🌌 <b><u>ᴄᴏᴍᴍᴇɴᴄᴇʀ ᴀᴠᴇᴄ ᴜɴᴇ ᴍɪɴɪᴀᴛᴜʀᴇ</u></b>
  
•> /start ᴜɴ ʙᴏᴛ ᴇᴛ ᴇɴᴠᴏʏᴇᴢ ᴜɴᴇ ɪᴍᴀɢᴇ ᴘᴏᴜʀ ᴅᴇғɪɴɪʀ ᴀᴜᴛᴏᴍᴀᴛɪᴄᴀʟʟʏ ʟᴀ ᴍɪɴɪᴀᴛᴜʀᴇ.
•> /delthumb ᴜᴛɪʟɪsᴇᴢ ᴄᴇᴛᴛᴇ ᴄᴏᴍᴍᴀɴᴅᴇ ᴘᴏᴜʀ sᴜᴘᴘʀɪᴍᴇʀ vᴏᴛʀᴇ ᴀɴᴄɪᴇɴɴᴇ ᴍɪɴɪᴀᴛᴜʀᴇ.
•> /viewthumb ᴜᴛɪʟɪsᴇᴢ ᴄᴇᴛᴛᴇ ᴄᴏᴍᴍᴀɴᴅᴇ ᴘᴏᴜʀ vᴏɪʀ vᴏᴛʀᴇ ᴍɪɴɪᴀᴛᴜʀᴇ ᴀᴄᴛᴜᴇʀᴇ.

📑 <b><u>ᴄᴏᴍᴍᴇɴᴄᴇʀ ᴀᴠᴇᴄ ᴜɴᴇ ʟᴇɢᴇɴᴅᴇ ᴘᴇʀsᴏɴɴᴀʟɪsᴇ́ᴇ</u></b>
•> /set_caption - ᴅᴇғɪɴɪʀ ᴜɴᴇ ʟᴇɢᴇɴᴅᴇ ᴘᴇʀsᴏɴɴᴀʟɪsᴇ́ᴇ
•> /see_caption - vᴏɪʀ vᴏᴛʀᴇ ʟᴇɢᴇɴᴅᴇ ᴘᴇʀsᴏɴɴᴀʟɪsᴇ́ᴇ
•> /del_caption - sᴜᴘᴘʀɪᴍᴇʀ ʟᴀ ʟᴇɢᴇɴᴅᴇ ᴘᴇʀsᴏɴɴᴀʟɪsᴇ́ᴇ

ᴇxᴀᴍᴘʟᴇ :- /set_caption 📕 ɴᴏᴍ ᴅᴜ ꜰɪʟᴇ : {filename}
💾 sɪᴢᴇ : {filesize}
⏰ ᴅᴜʀᴀᴛɪᴏɴ : {duration}

✏️ <b><u>ᴄᴏᴍᴍᴇɴᴄᴇʀ ᴀᴠᴇᴄ ᴜɴ ʀᴇɴᴏᴍᴍᴀɢᴇ</u></b>
•> ᴇɴᴠᴏʏᴇᴢ ᴜɴ ꜰɪʟᴇ ᴇᴛ ᴄʟɪqᴜᴇᴢ sᴜʀ ʟ'ᴏᴘᴛɪᴏɴ ᴅᴇ ʀᴇɴᴏᴍᴍᴀɢᴇ, ᴛᴀᴘᴇᴢ ʟᴇ ɴᴏᴜᴠᴇᴀᴜ ɴᴏᴍ ᴅᴜ ꜰɪʟᴇ ᴇᴛ \n sᴇʟᴇᴄᴛɪᴏɴɴᴇᴢ [ᴅᴏᴄᴜᴍᴇɴᴛ, vɪᴅᴇᴏ, ᴀᴜᴅɪᴏ] 👈 ᴄʜᴏɪssɪᴢᴇ ᴄᴇᴛᴛᴇ ᴄᴏᴍᴍᴀɴᴅᴇ.
ℹ️ ᴀɴʏ ᴏᴛʜᴇʀ ʜᴇʟᴘ ᴄᴏɴᴛᴀᴄᴛ :- <a href=https://t.me/hokageclub>𝑺𝑼𝑷𝑷𝑶𝑹𝑻 𝑮𝑹𝑶𝑼𝑷</a>
"""

#⚠️ ɴᴇ ʀᴇᴛɪʀᴇᴢ ᴘᴀs ɴᴏs ᴄʀᴇ́ᴅɪᴛs 🙏😢😢
    DEV_TXT = """
<b><u>ʀᴇᴍᴇʀᴄɪᴇᴍᴇɴᴛs spéᴄɪᴀᴜx & ᴅᴇᴠᴇʟᴏᴘᴇʀs</b></u> 

» ᴄᴏᴅᴇ sᴏᴜʀᴄᴇ : <a href=https://github.com/oVo-hyoshdesign/RENAME-PRO>𝐑𝐄𝐍𝐀𝐌𝐄 𝐁𝐎𝐓</a>
» ᴄᴏᴍᴍᴇɴᴛ ᴅᴇᴘʟᴏʏᴇʀ : <a href=https://youtu.be/>hyoshdesign</a>

• ❣️ <a href=https://github.com/oVo-hyoshdesign>oVo-hyoshdesign</a>
• ❣️ <a href=https://t.me/Hyoshdesign>Hyoshdesign</a>
• ❣️ <a href=https://youtube.com/@hyoshdesign>hyoshdesign YT</a>
"""
