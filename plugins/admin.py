#@Xyr33n
#Mohon jangan dihapus WM diatas dan jika ingin melakukan recoding sertakan sumber 

import array
import sys
import os
import time
import traceback
import asyncio
import shutil
import psutil
from datetime import datetime

import aiofiles
from pyrogram.types import CallbackQuery, Message
from functools import wraps

from pyrogram import Client, filters
from pyrogram.errors import RPCError
from config import *
from bot import Bot

	
	

@Bot.on_message(filters.command("logs") & filters.user(OWNER_ID))
async def logs_chat(_, message):
    time = (datetime.now()).strftime("%d/%m/%Y %H:%M:%S")
    caption = f"""
𝗪𝗮𝗸𝘁𝘂 : {time}
𝗧𝗶𝗽𝗲 𝗟𝗼𝗴 : 𝙴𝚛𝚛𝚘𝚛
"""
    try:
        await message.reply_document(
            LOG_FILE_NAME, caption=caption
        )
    except ValueError:
        await message.reply_text("**LOGS ARE EMPTY**")
        
        
@Bot.on_message(filters.user(ADMINS) & filters.command('ping'))
async def ping_signal(client: Client, message: Message):
    start = datetime.now()
    tauk = await message.reply('Pong!')
    end = datetime.now()
    m_s = (end - start).microseconds/ 1000
    await tauk.edit(f"<b>Pong! ⚡ </b>\n {m_s} ms")
    
  
@Bot.on_message(filters.command('help') & filters.private)
async def _help(client: Client, message: Message):
  await message.reply_text("""<b>Perintah utama :</b>
 •/start - memulai penggunaan bot
 •/help - melihat bantuan dan perintah bot
 •/id - melihat informasi mengenai id akun atau suatu group dan channel
 
<b>Bantuan untuk Admin :</b>
 •/batch - buat tautan untuk lebih dari satu postingan
 •/genlink - buat tautan untuk satu postingan
 •/logs - melihat info log bot pada 
 •/broadcast - melakukan pesan siaran ke semua pengguna bot
 •/admins - melihat daftar admin bot
 •/ping - melihat ping jaringan bot
 
 <b>Bantuan untuk OWNER Bot</b>
 •/promote - untuk mempromosikan pengguna menjadi admin bot dengan cara reply pesan pengguna atau dengan /promote @usernameAkun
 
𝗡𝗼𝘁𝗲: Untuk menggunakan bot Ini Kalian Wajib Join Channel & Group Yang sudah ditentukan 
""")
