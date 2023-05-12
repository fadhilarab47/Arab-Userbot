# if you can read this, this meant you use code from Geez | Ram Project
# this code is from somewhere else
# please dont hestitate to steal it
# because Geez and Ram doesn't care about credit
# at least we are know as well
# who Geez and Ram is
#
#
# kopas repo dan hapus credit, ga akan jadikan lu seorang developer
# ©2023 Geez | Ram Team
import random
from rams import app
from pyrogram import filters
from pyrogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from config import ID_OWNER as owner 

@app.on_callback_query()
def pmowner(client, callback_query):
    user_id = owner
    message = "Lu Siapa Anjeng!!!!"
    client.send_message(user_id, message)
    client.answer_callback_query(callback_query.id, text="Message sent")

ramslogo = [
    "https://telegra.ph/file/d03ce0fb84f81be3aeb09.png",
    "https://telegra.ph/file/200355acbe58c46400f5b.png",
    "https://telegra.ph/file/c78bb1efdeed38ee16eb2.png",
    "https://telegra.ph/file/4143843c984a8ecdc813e.png"
]

alive_logo = random.choice(ramslogo)

@app.on_message(filters.command("start") & filters.private)
async def start(app, message):
    chat_id = message.chat.id
    file_id = alive_logo
    caption = "Hi, Saya Asisstant Uputt-Project\nTidak Ada Yang Special Kecuali Indomie."
    reply_markup = InlineKeyboardMarkup([
        [
            InlineKeyboardButton("Support", url="https://t.me/UputtSupport"),
            InlineKeyboardButton("Channel", url="https://t.me/amneseey0u"),
        ],
    ])

    await app.send_photo(chat_id, file_id, caption=caption, reply_markup=reply_markup)
