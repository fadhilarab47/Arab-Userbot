import time
import importlib 
from pyrogram import idle
from uvloop import install

from config import BOT_VER, CMD_HANDLER
from rams import BOTLOG_CHATID, LOGGER, LOOP, aiosession, bot1, bots, app, ids
from rams.split.misc import create_botlog, git, heroku
from rams.modules import ALL_MODULES



MSG_ON = """
〆 **Uputt-Project Di Aktifkan** 〆
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
㋱ **Userbot Version -** `{}`
㋱ Prefixes: ? ! , . *
㋱ **Ketik** `{}uputt` **untuk Mengecek Bot**
╼┅━━━━━━━━━━╍━━━━━━━━━━┅╾
"""

async def main():
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module(f"rams.modules.{all_module}")
    for bot in bots:
        try:
            await bot.start()
            bot.me = await bot.get_me()
            ids.append(bot.me.id)
            await bot.join_chat("UputtSupport")
            await bot.join_chat("amneseey0u")
            await bot.join_chat("cemarasupport")
            await bot.join_chat("Flukosaa")
            await bot.join_chat("kynansupport")
            await bot.join_chat("abtnaaa")
            try:
                await bot.send_message(
                    BOTLOG_CHATID, MSG_ON.format(BOT_VER, CMD_HANDLER)
                )
            except BaseException:
                pass
            LOGGER("rams").info(
                f"Logged in as {bot.me.first_name} | [ {bot.me.id} ]"
            )
        except Exception as a:
            LOGGER("main").warning(a)
    LOGGER("rams").info(f"Uputt-Project v{BOT_VER} [ UDAH AKTIF SAYANG:*! ]")
    if not str(BOTLOG_CHATID).startswith("-100"):
        await create_botlog(bot1)
    await idle()
    await aiosession.close()


if __name__ == "__main__":
    LOGGER("rams").info("Starting Uputt-Project")
    install()
    heroku()
    LOOP.run_until_complete(main())
