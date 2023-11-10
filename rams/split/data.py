from pyrogram.types import InlineKeyboardButton, WebAppInfo
from rams import CMD_HELP
modules = CMD_HELP
class Data:

    text_help_menu = (
        f"**Menu Inline sɪ ᴧꝛᴧʙ-ᴜsᴇʀʙᴏᴛ**\n**Perintah :** ? ! . * , $"
        .replace(",", "")
        .replace("[", "")
        .replace("]", "")
        .replace("'", "")
    )
    reopen = [[InlineKeyboardButton("ᴘᴇɴᴄᴇᴛ ᴀᴊᴀ", callback_data="reopen")]]
