from config import * 
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from helper.database import botdata, find_one, total_user, getid
from helper.database import dbcol
from helper.progress import humanbytes
from datetime import datetime, timezone

token = BOT_TOKEN
botid = token.split(':')[0]

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["users"]))
async def users(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    id = str(getid())
    ids = id.split(',')

    await message.reply_text(
        f"⚡️ **Uᴛɪʟɪsᴀᴛᴇᴜʀs Tᴏᴛᴀᴜx** :- {total_user()}\n\n"
        f"⚡️ **Tᴏᴛᴀʟ Dᴇ Fɪʟs Rᴇɴᴏᴍᴍés** :- {total_rename}\n"
        f"⚡ **Tᴀɪʟʟᴇ Tᴏᴛᴀʟᴇ Dᴇs Fɪʟs Rᴇɴᴏᴍᴍés** :- {humanbytes(int(total_size))}",
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Fᴇʀᴍᴇʀ 🦋", callback_data="cancel")]])
    )

@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["allids"]))
async def allids(client, message):
    botdata(int(botid))
    data = find_one(int(botid))
    total_rename = data["total_rename"]
    total_size = data["total_size"]
    
    raw_ids = str(getid())  
    raw_ids = raw_ids.replace('[', '').replace(']', '').replace(' ', '')  
    ids = [id.strip() for id in raw_ids.split(',') if id.strip().isdigit()] 

    user_details = []
    for user_id in ids:
        try:
            user = await client.get_users(int(user_id)) 
            username = user.username if user.username else "Aucun username"
            user_details.append(f"• `{user_id}` - @{username}")
        except Exception as e:
            user_details.append(f"• `{user_id}` - [Erreur : {e}]")

    user_list = "\n".join(user_details)
    
    additional_info = (
        f"⚡️ **Uᴛɪʟɪsᴀᴛᴇᴜʀs Tᴏᴛᴀᴜx** :- {total_user()}\n\n"
        f"⚡️ **Tᴏᴛᴀʟ Dᴇ Fɪʟs Rᴇɴᴏᴍᴍés** :- {total_rename}\n"
        f"⚡ **Tᴀɪʟʟᴇ Tᴏᴛᴀʟᴇ Dᴇs Fɪʟs Rᴇɴᴏᴍᴍés** :- {humanbytes(int(total_size))}"
    )
    
    max_message_length = 4096
    message_parts = []

    while len(user_list) > max_message_length:
        part = user_list[:max_message_length]
        user_list = user_list[max_message_length:]
        message_parts.append(part)
    if user_list:
        message_parts.append(user_list)

    for part in message_parts:
        await message.reply_text(f"⚡️ **Liste des utilisateurs avec IDs :**\n{part}\n\n{additional_info}", quote=True,
                                 reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Fᴇʀᴍᴇʀ 🦋", callback_data="cancel")]]))


@Client.on_message(filters.private & filters.user(OWNER) & filters.command(["subs"]))
async def subscriptions(client, message):
    users = dbcol.find()

    basic_users = []
    standard_users = []
    pro_users = []

    for user in users:
        user_id = user["_id"]
        user_type = user.get("usertype", "Free")
        expiration_unix = user.get("prexdate", None)

        if expiration_unix and isinstance(expiration_unix, int):
            expiration_date = datetime.fromtimestamp(expiration_unix, tz=timezone.utc).strftime("%d-%m-%Y")
        else:
            expiration_date = "Aucune"

        user_info = f"• `{user_id}` - {user_type} - ᴇxᴘɪʀᴀᴛɪᴏɴ : {expiration_date}\n"

        if user_type == "🪙 Bᴀsɪᴄ":
            basic_users.append(user_info)
        elif user_type == "⚡ Sᴛᴀɴᴅᴀʀᴅ":
            standard_users.append(user_info)
        elif user_type == "💎 Pʀᴏ":
            pro_users.append(user_info)

    response = "📋 **ʟɪꜱᴛᴇ ᴅᴇꜱ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀꜱ ᴘᴀʀ ᴀʙᴏɴɴᴇᴍᴇɴᴛ :**\n\n"
    if basic_users:
        response += "**🪙 Bᴀsɪᴄ**\n" + "".join(basic_users) + "\n"
    if standard_users:
        response += "**⚡ Sᴛᴀɴᴅᴀʀᴅ**\n" + "".join(standard_users) + "\n"
    if pro_users:
        response += "**💎 Pʀᴏ**\n" + "".join(pro_users) + "\n"

    if not basic_users and not standard_users and not pro_users:
        response += "ᴀᴜᴄᴜɴ ᴜᴛɪʟɪꜱᴀᴛᴇᴜʀ ᴛʀᴏᴜᴠé ᴀᴠᴇᴄ ᴅᴇꜱ ᴀʙᴏɴɴᴇᴍᴇɴᴛꜱ ᴀᴄᴛɪꜰꜱ."

    await message.reply_text(
        response,
        quote=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🦋 Fᴇʀᴍᴇʀ 🦋", callback_data="cancel")]])
    )