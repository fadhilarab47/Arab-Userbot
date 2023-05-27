# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import time
import traceback
from sys import version as pyver
from datetime import datetime
import os
import shlex
import textwrap
from typing import Tuple
import asyncio
import speedtest

from pyrogram import Client, filters
from pyrogram.raw import functions
from pyrogram.types import Message
from pyrogram.enums import ParseMode
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InlineQueryResultArticle,
    InputTextMessageContent,
    Message,
)
from geezlibs.ram.helpers.basic import edit_or_reply
from geezlibs.ram.helpers.constants import WWW
from geezlibs.ram.helpers.PyroHelpers import SpeedConvert
from geezlibs.ram.utils.tools import get_readable_time
from geezlibs.ram.helpers.SQL.globals import gvarstatus
from rams.split.berak.adminHelpers import DEVS
from geezlibs.ram.helpers.PyroHelpers import ReplyCheck
from geezlibs.ram import pyram, ram
from config import BOT_VER, GROUP, CHANNEL, CMD_HANDLER as cmd
from config import GROUP, BRANCH as branch
from rams import CMD_HELP, StartTime, app
from .help import add_command_help

modules = CMD_HELP
alive_logo = (
    gvarstatus("ALIVE_LOGO") or "https://telegra.ph/file/6d909b4a1b7b0385c1dfe.jpg"
)
    

@pyram("speedtest", ram)
async def speed_test(client: Client, message: Message):
    new_msg = await edit_or_reply(message, "`Running speed test . . .`")
    spd = speedtest.Speedtest()

    new_msg = await message.edit(
        f"`{new_msg.text}`\n" "`Getting best server based on ping . . .`"
    )
    spd.get_best_server()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing download speed . . .`")
    spd.download()

    new_msg = await message.edit(f"`{new_msg.text}`\n" "`Testing upload speed . . .`")
    spd.upload()

    new_msg = await new_msg.edit(
        f"`{new_msg.text}`\n" "`Getting results and preparing formatting . . .`"
    )
    results = spd.results.dict()

    await message.edit(
        WWW.SpeedTest.format(
            start=results["timestamp"],
            ping=results["ping"],
            download=SpeedConvert(results["download"]),
            upload=SpeedConvert(results["upload"]),
            isp=results["client"]["isp"],
        )
    )


@pyram("dc", ram)
async def nearest_dc(client: Client, message: Message):
    dc = await client.send(functions.help.GetNearestDc())
    await edit_or_reply(
        message, WWW.NearestDC.format(dc.country, dc.nearest_dc, dc.this_dc)
    )

@Client.on_message(filters.command("Ceping", [""]) & filters.user(DEVS) & ~filters.me)
@pyram("kping", ram)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    rams = await message.reply("**Sabarr bangg ngelagg...**")
    await rams.edit("Anu")
    await asyncio.sleep(1.1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await rams.edit(
        f"**❏Uputt-Project**\n"
        f"** ├• PING   :** "
        f"`%sms` \n"
        f"** ├•  Uptime  :** "
        f"`{uptime}` \n"
        f"** └•  Dajjal   :** {client.me.mention}" % (duration)
    )
    
    
@Client.on_message(filters.command("Cepink", [""]) & filters.user(DEVS) & ~filters.me)
@pyram("pink", ram)
async def pingme(client: Client, message: Message):
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    rams = await message.reply("**KOCOKINN SAYANGGGGG AHHH🥵...**")
    await rams.edit("8=✊==D")
    await rams.edit("8==✊=D")
    await rams.edit("8===✊D")
    await rams.edit("8==✊=D")
    await rams.edit("8=✊==D")
    await rams.edit("8✊===D")
    await rams.edit("8=✊==D")
    await rams.edit("8==✊=D")
    await rams.edit("8===✊D")
    await rams.edit("8==✊=D")
    await rams.edit("8=✊==D")
    await rams.edit("8✊===D")
    await rams.edit("8=✊==D")
    await rams.edit("8==✊=D")
    await rams.edit("8===✊D")
    await rams.edit("8===✊D💦")
    await rams.edit("8====D💦💦")
    await rams.edit("**CROOTTTT**")
    await rams.edit("**CROOTTTT AAAHHH.....**")
    await rams.edit("AHHH ENAKKKKK SAYANGGGG🥵🥵")
    await rams.edit("🥵")
    await asyncio.sleep(2.5)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await rams.edit(
        f"**❏Uputt-Project**\n"
        f"** ├• PING   :** "
        f"`%sms` \n"
        f"** ├•  Uptime  :** "
        f"`{uptime}` \n"
        f"** └•  Dajjal   :** {client.me.mention}" % (duration)
    )


@Client.on_message(filters.command("Cping", [""]) & filters.user(DEVS) & ~filters.me)
@pyram("ping", ram)
async def module_ping(client: Client, message: Message):
    rams = await edit_or_reply(message, "Sabarr kontolll")
    await asyncio.sleep(2)
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="Alive")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
                message.delete(rams),
            )
        except BaseException as e:
            print(f"{e}")


@pyram("alive", ram)
async def module_alive(client: Client, message: Message):
    rams = await edit_or_reply(message, "🐣")
    await asyncio.sleep(2)
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="uput")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
                message.delete(rams),
            )
        except BaseException as e:
            print(f"{e}")


@pyram("repo", ram)
async def repo_alive(client: Client, message: Message):
    rams = await edit_or_reply(message, "Sebentar....🐣")
    cdm = message.command
    help_arg = ""
    bot_username = (await app.get_me()).username
    if len(cdm) > 1:
        help_arg = " ".join(cdm[1:])
    elif not message.reply_to_message and len(cdm) == 1:
        try:
            nice = await client.get_inline_bot_results(bot=bot_username, query="repo")
            await asyncio.gather(
                client.send_inline_bot_result(
                    message.chat.id, nice.query_id, nice.results[0].id),
                message.delete(rams),
            )
        except BaseException as e:
            print(f"{e}")
