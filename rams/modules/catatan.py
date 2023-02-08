
from asyncio import sleep
from pyrogram import Client, filters


from rams import BOTLOG_CHATID
from geezlibs.ram.helpers.SQL.notes_sql import add_note, get_note, get_notes, rm_note
from geezlibs.ram.helpers.tools import get_arg

cmd = [",", ".", "?", "*", "!" "$",]

@Client.on_message(filters.command("notes", cmd) & filters.me)
async def list_notes(client, message):
    user_id = message.from_user.id
    notes = get_notes(str(user_id))
    if not notes:
        return await message.reply("Tidak ada catatan.")
    msg = f"Daftar catatan\n"
    for note in notes:
        msg += f"* {note.keyword}\n"
    await message.reply(msg)


@Client.on_message(filters.command("clear", cmd) & filters.me)
async def remove_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    if rm_note(str(user_id), notename) is False:
        return await message.reply(
            "Tidak dapat menemukan catatan: {}".format(notename)
        )
    return await message.reply("Berhasil Menghapus Catatan: {}".format(notename))


@Client.on_message(filters.command("save", cmd) & filters.me)
async def simpan_note(client, message):
    keyword = get_arg(message)
    user_id = message.from_user.id
    msg = message.reply_to_message
    if not msg:
        return await message.reply("Tolong balas ke pesan")
    anu = await msg.forward("me")
    msg_id = anu.id
    await client.send_message(
        "me",
        f"#NOTE\nKEYWORD: {keyword}"
        "\n\nPesan berikut disimpan sebagai data balasan catatan untuk obrolan, mohon JANGAN dihapus !!",
    )
    await sleep(2)
    add_note(str(user_id), keyword, msg_id)
    await message.reply(f"Berhasil menyimpan note {keyword}")


@Client.on_message(filters.command("get", cmd) & filters.me)
async def panggil_notes(client, message):
    notename = get_arg(message)
    user_id = message.from_user.id
    note = get_note(str(user_id), notename)
    if not note:
        return await message.reply("Tidak ada catatan seperti itu.")
    msg_o = await client.get_messages("me", int(note.f_mesg_id))
    await msg_o.copy(message.chat.id, reply_to_message_id=message.id)
