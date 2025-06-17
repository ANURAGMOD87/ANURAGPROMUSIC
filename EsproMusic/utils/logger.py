from pyrogram.enums import ParseMode

from EsproMusic import app
from EsproMusic.utils.database import is_on_off
from config import LOGGER_ID


async def play_logs(message, streamtype):
    if await is_on_off(2):
        chat_members = await app.get_chat_members_count(message.chat.id)
        async for admin in app.get_chat_members(message.chat.id, filter=enums.ChatMembersFilter.ADMINISTRATORS):
            if admin.status == enums.ChatMemberStatus.OWNER:
                owner_ISTKHARBOT = admin.user.mention if hasattr(admin.user, 'mention') and admin.user.mention else "Is_Hide / Deleted"
                owner_ISTKHARBOT_id = admin.user.id if hasattr(admin.user, 'id') else "Is_Hide / Deleted"
        logger_text = f"""
<b>{app.mention} ᴘʟᴀʏ ʟᴏɢ</b>
╔════❰𝐏𝐋𝐀𝐘𝐈𝐍𝐆❱═══❍⊱❁۪۪
<b>◈ 𝐂𝐡𝐚𝐭 ➪ </b>{message.chat.title}
<b>◈ 𝐂𝐡𝐚𝐭 𝐈𝐝 ➪ </b> <code>{message.chat.id}</code>
<b>◈ 𝐔𝐬𝐞𝐫 ➪ </b> {message.from_user.mention}
<b>◈ 𝐔𝐬𝐞𝐫𝐧𝐚𝐦𝐞 ➪ </b> @{message.from_user.username}
<b>◈ 𝐈𝐝 ➪ </b> <code>{message.from_user.id}</code>
<b>◈ 𝐂𝐡𝐚𝐭 𝐋𝐢𝐧𝐤 ➪ </b> @{message.chat.username}
<b>◈ 𝐂𝗵𝗮𝘁 𝗠𝗲𝗺𝗯𝗲𝗿𝘀 ➪ </b> <code>{chat_members}</code>
<b>◈ 𝐂𝗵𝗮𝘁 𝗢𝘄𝗻𝗲𝗿 ➪ </b> {owner_ISTKHARBOT} 𝐈𝐝 ➪<code>{owner_ISTKHARBOT_id}</code>
<b>◈ 𝐒𝐞𝐚𝐫𝐜𝐡𝐞𝐝 ➪ </b> <code>{message.text.split(None, 1)[1]}</code>
<b>◈ 𝐁𝐲 ➪ </b> {streamtype}
╚═══❰ #𝐍𝐞𝐰𝐒𝐨𝐧𝐠 ❱══❍⊱❁۪۪"""
        if message.chat.id != LOG_GROUP_ID:
            try:
                await app.send_message(
                    chat_id=LOG_GROUP_ID,
                    text=logger_text,
                    parse_mode=ParseMode.HTML,
                    disable_web_page_preview=True,
                )
            except:
                pass
        return
