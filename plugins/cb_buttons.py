import os

if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config

from plugins.commands import start, help
from plugins.youtube_dl_button import youtube_dl_call_back
from plugins.dl_button import ddl_call_back
from translation import Translation
from pyrogram import Client
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_callback_query()
async def button(bot, update):
    if "|" in update.data:
        await youtube_dl_call_back(bot, update)

    elif "=" in update.data:
        await ddl_call_back(bot, update)

    elif update.data == "close":
        await update.message.delete()
