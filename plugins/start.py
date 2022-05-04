# (©)Codexbotz


import asyncio
from datetime import datetime
from time import time

from pyrogram import Client, filters
from pyrogram.errors import FloodWait, InputUserDeactivated, UserIsBlocked
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from bot import Bot
from config import ADMINS, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, FORCE_MSG, START_MSG, OWNER_USERNAME, CAPTION_SATU, CAPTION_DUA,  CAPTION_TIGA
from database.sql import add_user, full_userbase, query_msg
from helper_func import decode, get_messages, subscribed



@Bot.on_message(filters.command("start") & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    user_name = "@" + message.from_user.username if message.from_user.username else None
    try:
        await add_user(id, user_name)
    except:
        pass
    text = message.text
    if len(text) > 7:
        try:
            base64_string = text.split(" ", 1)[1]
        except BaseException:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except BaseException:
                return
            if start <= end:
                ids = range(start, end + 1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except BaseException:
                return
        temp_msg = await message.reply("<code>Sedang Memproses Mohon Tunggu...</code>")
        try:
            messages = await get_messages(client, ids)
        except BaseException:
            await message.reply_text("<b>Telah Terjadi suatu kesalahan silakan cek /logs apa yang sedang terjadi...</b>🥺")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(
                    previouscaption="" if not msg.caption else msg.caption.html,
                    filename=msg.document.file_name,
                )
            else:
                caption = "" if not msg.caption else msg.caption.html

            reply_markup = msg.reply_markup if DISABLE_CHANNEL_BUTTON else None
            try:
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode="html",
                    reply_markup=reply_markup,
                )
                await asyncio.sleep(0.5)
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode="html",
                    reply_markup=reply_markup,
                )
            except BaseException:
                pass
    else:
        buttons = [
            [
                 InlineKeyboardButton("OWNER BOT", url=OWNER_USERNAME)
            ], 
            [
                InlineKeyboardButton(CAPTION_SATU, url=client.invitelink),
                InlineKeyboardButton(CAPTION_DUA, url=client.invitelink2)
            ],
            [
                InlineKeyboardButton(CAPTION_TIGA, url=client.invitelink3)
            ]
        ]
        await message.reply_text(
            text=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None
                if not message.from_user.username
                else "@" + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id,
            ),
            reply_markup=InlineKeyboardMarkup(buttons),
            disable_web_page_preview=True,
            quote=True,
        )

    return


@Bot.on_message(filters.command("start") & filters.private)
async def not_joined(client: Client, message: Message):
    buttons = [
            [
                InlineKeyboardButton(CAPTION_SATU, url=client.invitelink),
                InlineKeyboardButton(CAPTION_DUA, url=client.invitelink2),
            ],
            [
                InlineKeyboardButton(CAPTION_TIGA, url=client.invitelink3),
            ],
        ]
    try:
        buttons.append(
        [
            InlineKeyboardButton("RELOAD FILE", url=f"https://t.me/{client.username}?start={message.command[1]}",
            )
         ]
     )
    except IndexError:
        pass

    await message.reply(
        text=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None
            if not message.from_user.username
            else "@" + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id,
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True,
    )


@Bot.on_message(filters.command("users") & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(
        chat_id=message.chat.id, text="<code>Sedang melihat data pengguna bot ...</code>"
    )
    users = await full_userbase()
    await msg.edit(f"{len(users)} <b>Total pengguna yang menggunakan bot ini</b>")


@Bot.on_message(filters.private & filters.command("broadcast") & filters.user(ADMINS))
async def send_text(client: Bot, message: Message):
    if message.reply_to_message:
        query = await query_msg()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0

        pls_wait = await message.reply(
            "<code>Melakukan pesan siaran ke semua pengguna bot...</code>"
        )
        for row in query:
            chat_id = int(row[0])
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                blocked += 1
            except InputUserDeactivated:
                deleted += 1
            except BaseException:
                unsuccessful += 1
            total += 1

        status = f"""<b><u>Berhasil Melakukan Broadcast</u></b>
Jumlah Pengguna: <code>{total}</code>
Berhasil: <code>{successful}</code>
Gagal: <code>{unsuccessful}</code>
Pengguna diblokir: <code>{blocked}</code>
Akun Terhapus: <code>{deleted}</code></b>"""

        return await pls_wait.edit(status)

    else:
        msg = await message.reply(
            "<code>Mohon maaf silakan reply pesan lalu lakukan dengan /broadcast.</code>"
        )
        await asyncio.sleep(8)
        await msg.delete()





