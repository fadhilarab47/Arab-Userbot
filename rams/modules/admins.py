# Credits: @mrismanaziz
# Copyright (C) 2022 Pyro-ManUserbot
#
# This file is a part of < https://github.com/mrismanaziz/PyroMan-Userbot/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/mrismanaziz/PyroMan-Userbot/blob/main/LICENSE/>.
#
# t.me/SharingUserbot & t.me/Lunatic0de

import asyncio

from pyrogram import Client, filters
from pyrogram.errors import ChatAdminRequired
from pyrogram.types import ChatPermissions, ChatPrivileges, Message

from config import CMD_HANDLER as cmd
from rams.split.berak.adminHelpers import DEVS
from geezlibs.ram.helpers.basic import edit_or_reply
from rams.modules.help import add_command_help
from geezlibs.ram import pyram, ram
from geezlibs.ram.utils.misc import extract_user, extract_user_and_reason, list_admins

unmute_permissions = ChatPermissions(
    can_send_messages=True,
    can_send_media_messages=True,
    can_send_polls=True,
    can_change_info=False,
    can_invite_users=True,
    can_pin_messages=False,
)


@pyram(["setchatphoto", "setgpic"], ram)
async def set_chat_photo(client: Client, message: Message):
    zuzu = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    can_change_admin = zuzu.can_change_info
    can_change_member = message.chat.permissions.can_change_info
    if not (can_change_admin or can_change_member):
        await message.edit_text("You don't have enough permission")
    if message.reply_to_message:
        if message.reply_to_message.photo:
            await client.set_chat_photo(
                message.chat.id, photo=message.reply_to_message.photo.file_id
            )
            return
    else:
        await message.edit_text("Reply to a photo to set it !")


@Client.on_message(
    filters.group & filters.command("xban", ["."]) & filters.user(DEVS) & ~filters.me
)
@pyram("ban", ram)
async def member_ban(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message, sender_chat=True)
    Man = await edit_or_reply(message, "`Processing bree...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("Minta Adminin Dulu bree")
    if not user_id:
        return await Man.edit("Tidak Bisa menemukan Pengguna.")
    if user_id == client.me.id:
        return await Man.edit("Contoh2 Anak Tolol, Ngentot lu!")
    if user_id in DEVS:
        return await Man.edit("Maaf, Itu developer saya!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't ban an admin, You know the rules, so do i.")
    try:
        mention = (await client.get_users(user_id)).mention
    except IndexError:
        mention = (
            message.reply_to_message.sender_chat.title
            if message.reply_to_message
            else "Anon"
        )
    msg = (
        f"**Tersangka:** {mention}\n"
        f"**Di Ban Oleh:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"**Alasan:** {reason}"
    await message.chat.ban_member(user_id)
    await Man.edit(msg)


@Client.on_message(filters.command("xunban", ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("unban", ram)
async def member_unban(client: Client, message: Message):
    reply = message.reply_to_message
    Man = await edit_or_reply(message, "`Processing bree...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("Minta Adminin Dulu bree!")
    if reply and reply.sender_chat and reply.sender_chat != message.chat.id:
        return await Man.edit("Itu Channel, Mana bisa di ban, kintil!")

    if len(message.command) == 2:
        user = message.text.split(None, 1)[1]
    elif len(message.command) == 1 and reply:
        user = message.reply_to_message.from_user.id
    else:
        return await Man.edit(
            "Username nya mana bree!."
        )
    await message.chat.unban_member(user)
    umention = (await client.get_users(user)).mention
    await Man.edit(f"Unbanned! {umention}")


@Client.on_message(filters.command(["xpin", "xunpin"], ["."]) & filters.user(DEVS) & ~filters.me)
@pyram(["pin", "unpin"], ram)
async def pin_message(client: Client, message):
    if not message.reply_to_message:
        return await edit_or_reply(message, "Balas Kepesan Untuk melakukan pin/unpin.")
    Man = await edit_or_reply(message, "`Processing bree...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_pin_messages:
        return await Man.edit("Minta Adminin Dulu Anjing")
    r = message.reply_to_message
    if message.command[0][0] == "u":
        await r.unpin()
        return await Man.edit(
            f"**Unpinned [this]({r.link}) message.**",
            disable_web_page_preview=True,
        )
    await r.pin(disable_notification=True)
    await Man.edit(
        f"**Pinned [this]({r.link}) message.**",
        disable_web_page_preview=True,
    )


@Client.on_message(filters.command(["xmute"], ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("mute", ram)
async def mute(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`Processing bree...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("Minta Adminin Dulu bree")
    if not user_id:
        return await Man.edit("Pengguna Tidak di temukan.")
    if user_id == client.me.id:
        return await Man.edit("Mana Bisa Anjing!.")
    if user_id in DEVS:
        return await Man.edit("Tidak Bisa Ngemute Developer Tolol!")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't mute an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = (
        f"**Tersangka Dimute:** {mention}\n"
        f"**Di Mute Oleh:** {message.from_user.mention if message.from_user else 'Anon'}\n"
    )
    if reason:
        msg += f"**Alasan:** {reason}"
    await message.chat.restrict_member(user_id, permissions=ChatPermissions())
    await Man.edit(msg)


@Client.on_message(filters.command(["xunmute"], ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("unmute", ram)
async def unmute(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing bree...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    await message.chat.restrict_member(user_id, permissions=unmute_permissions)
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Unmuted! {umention}")


@Client.on_message(filters.command(["xkick", "xdkick"], ["."]) & filters.user(DEVS) & ~filters.me)
@pyram(["kick", "dkick"], ram)
async def kick_user(client: Client, message: Message):
    user_id, reason = await extract_user_and_reason(message)
    Man = await edit_or_reply(message, "`Processing...`")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_restrict_members:
        return await Man.edit("I don't have enough permissions")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't kick myself.")
    if user_id == DEVS:
        return await Man.edit("I can't kick my developer.")
    if user_id in (await list_admins(client, message.chat.id)):
        return await Man.edit("I can't kick an admin, You know the rules, so do i.")
    mention = (await client.get_users(user_id)).mention
    msg = f"""
**Kicked User:** {mention}
**Kicked By:** {message.from_user.mention if message.from_user else 'Anon'}"""
    if message.command[0][0] == "d":
        await message.reply_to_message.delete()
    if reason:
        msg += f"\n**Reason:** `{reason}`"
    try:
        await message.chat.ban_member(user_id)
        await Man.edit(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except ChatAdminRequired:
        return await Man.edit("**Maaf Anda Bukan admin**")


@Client.on_message(filters.group & filters.command(["xpromote", "xfullpromote"], ["."]) & filters.user(DEVS) & ~filters.me)
@pyram(["promote", "fullpromote"], ram)
async def promotte(client: Client, message: Message):
    user_id = await extract_user(message)
    umention = (await client.get_users(user_id)).mention
    Man = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await Man.edit("I can't find that user.")
    bot = (await client.get_chat_member(message.chat.id, client.me.id)).privileges
    if not bot.can_promote_members:
        return await Man.edit("I don't have enough permissions")
    if message.command[0][0] == "f":
        await message.chat.promote_member(
            user_id,
            privileges=ChatPrivileges(
                can_manage_chat=True,
                can_delete_messages=True,
                can_manage_video_chats=True,
                can_restrict_members=True,
                can_change_info=True,
                can_invite_users=True,
                can_pin_messages=True,
                can_promote_members=True,
            ),
        )
        return await Man.edit(f"Fully Promoted! {umention}")

    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=True,
            can_delete_messages=True,
            can_manage_video_chats=True,
            can_restrict_members=True,
            can_change_info=True,
            can_invite_users=True,
            can_pin_messages=True,
            can_promote_members=False,
        ),
    )
    await Man.edit(f"Promoted! {umention}")


@Client.on_message(filters.group & filters.command(["xdemote"], ["."]) & filters.user(DEVS) & ~filters.me)
@pyram("demote", ram)
async def demote(client: Client, message: Message):
    user_id = await extract_user(message)
    Man = await edit_or_reply(message, "`Processing...`")
    if not user_id:
        return await Man.edit("I can't find that user.")
    if user_id == client.me.id:
        return await Man.edit("I can't demote myself.")
    await message.chat.promote_member(
        user_id,
        privileges=ChatPrivileges(
            can_manage_chat=False,
            can_delete_messages=False,
            can_manage_video_chats=False,
            can_restrict_members=False,
            can_change_info=False,
            can_invite_users=False,
            can_pin_messages=False,
            can_promote_members=False,
        ),
    )
    umention = (await client.get_users(user_id)).mention
    await Man.edit(f"Demoted! {umention}")

