"""
Credit by Geez & SiArab
"""

import os
import shutil
import requests
import shlex
import asyncio
from typing import Tuple
from pyrogram import Client
from py_extract import Video_tools
from pyrogram.types import Message
from pyrogram.enums import MessageMediaType
from geezlibs.ram.utils.extra import shell_exec
from geezlibs.ram.helpers import ReplyCheck
from geezlibs.ram import pyram, ram

@pyram("aud", ram)
async def extract_aud(client: Client, message: Message):
    replied_msg = message.reply_to_message
    pcs_msg = await message.reply("`Mendownload Media ...`")
    ext_out_path = os.getcwd() + "downloads/"
    if not replied_msg:
        await pcs_msg.edit("**Mohon Balas Ke Video**")
        return
    if not replied_msg.video:
        await pcs_msg.edit("**Mohon Balas Ke Video**")
        return
    if not os.path.exists(ext_out_path):
        await pcs_msg.edit("Processing.....")
    else:
        await pcs_msg.edit("Extraction in progress. Please wait.")
        return
    replied_video = replied_msg.video
    try:
        await pcs_msg.edit("`Downloading...`")
        ext_video = await client.download_media(message=replied_video)
        if not os.path.isfile(ext_video):
            await pcs_msg.edit("`Error: Invalid file path`")
            return
        await pcs_msg.edit("`Extracting Audio...`")
        exted_aud = Video_tools.extract_all_audio(input_file=ext_video, output_path=ext_out_path)
        await pcs_msg.edit("`Uploading...`")
        for geez_aud in exted_aud:
            await message.reply_audio(audio=geez_aud, caption=f"`Extracted by` {(await client.get_me()).mention}")
        await pcs_msg.edit("`Extracting Finished!`")
        shutil.rmtree(ext_out_path)
        print(f"Deleted directory: {ext_out_path}")
    except Exception as e:
        await pcs_msg.edit(f"**Error:** `{e}`")


@pyram("rmbg", ram)
async def rmbg_background(client: Client, message: Message):
    api_key = "Zm5pBkqTUg9JQnSrZSJwaF2j"
    reply = message.reply_to_message
    await message.reply("`Processing..")
    photo_id = message.reply_to_message.photo.file_id
    if not (reply and (reply.media)):
        return await message.edit("`Mohon balas ke foto...`")
    temp_file = await client.download_media(photo_id)
    if not api_key:
        return await message.edit("**harap masukan RMBG API KEY di vars**")
    endpoint = "https://api.remove.bg/v1.0/removebg"
    payload = {"size": "auto"}

    if api_key:
        with open(temp_file, "rb") as image_file:
            response = requests.post(endpoint, data=payload, headers={"X-Api-Key": api_key}, files={"image_file": image_file}, stream=True)

    with open("output.png", "wb") as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response
    await message.reply_document("output.png")
    try:
        clear_file = "output.webp"
        clear_file2 = "output.png"
        (await shell_exec("cp *.png *.webp"))[0]
        await client.send_sticker(message.chat.id, "output.webp")
        os.remove(clear_file)
        os.remove(clear_file2)
    except BaseException:
        pass


async def run_cmd(cmd: str) -> Tuple[str, str, int, int]:
    """Run Commands"""
    args = shlex.split(cmd)
    process = await asyncio.create_subprocess_exec(
        *args, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    return (
        stdout.decode("utf-8", "replace").strip(),
        stderr.decode("utf-8", "replace").strip(),
        process.returncode,
        process.pid,
    )
