# (©)Codexbotz

import pyromod.listen
import sys

from pyrogram import Client

from config import (
    API_HASH,
    APP_ID,
    CHANNEL_ID,
    FORCE_SUB_SATU,
    FORCE_SUB_DUA,
    FORCE_SUB_TIGA, 
    LOGGER,
    OWNER_USERNAME,
    BOT_TOKEN,
    TG_BOT_WORKERS,
)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=BOT_TOKEN,
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()

        if FORCE_SUB_SATU:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_SATU)
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan  FORCE_SUB_SATU!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali nilai FORCE_SUB_SATU dan Pastikan Bot anda Admin di Channel dengan izin dapat mengundang melalui tautan undangan, nilai FORCE_SUB_SATU   Saat Ini: {FORCE_SUB_SATU}"
                )
                self.LOGGER(__name__).info(
                    "\nBot Telah Berhenti."
                )
                sys.exit()
        if FORCE_SUB_DUA:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_DUA)
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_DUA!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali nilai FORCE_SUB_DUA dan Pastikan Bot anda Admin di Channel dengan izin dapat mengundang melalui tautan undangan,  nilai FORCE_SUB_DUA Saat Ini: {FORCE_SUB_DUA}"
                )
                self.LOGGER(__name__).info(
                    "\nBot telah berhenti."
                )
                sys.exit()
        if FORCE_SUB_TIGA:
            try:
                link = await self.export_chat_invite_link(FORCE_SUB_TIGA)
                self.invitelink3 = link
            except Exception as a:
                self.LOGGER(__name__).warning(a)
                self.LOGGER(__name__).warning(
                    "Bot tidak dapat Mengambil link Undangan dari FORCE_SUB_TIGA!"
                )
                self.LOGGER(__name__).warning(
                    f"Silakan periksa kembali nilai FORCE_SUB_TIGA dan Pastikan Bot anda Admin di Channel dengan izin dapat mengundang melalui tautan undangan, FORCE_SUB_TIGA Saat Ini: {FORCE_SUB_TIGA}"
                )
                self.LOGGER(__name__).info(
                    "\nBot telah Berhenti."
                )
                sys.exit()
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(
                f"Pastikan Bot adalah Admin di Channel DataBase, dan Periksa kembali Nilai CHANNEL_ID, Database Saat Ini: {CHANNEL_ID}"
            )
            self.LOGGER(__name__).info(
                "\nBot telah Berhenti."
            )
            sys.exit()

        self.set_parse_mode("html")
        self.LOGGER(__name__).info(
            f"[🔥 BOT TELAH AKTIF! 🔥]\n\nBOT Dibuat oleh @{OWNER_USERNAME}\nJika terjadi suatu kesalahan atau eror kamu bisa bertanya ke group https://t.me/shakeinsayang"
        )
        self.username = usr_bot_me.username

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Ops, Bot berhenti!!!.")
