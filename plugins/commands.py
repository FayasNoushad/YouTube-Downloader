import os
if bool(os.environ.get("WEBHOOK", False)):
    from sample_config import Config
else:
    from config import Config
from translation import Translation
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.command(["start", "help"]) & filters.private)
async def start(bot, update):
    await bot.send_message(
        chat_id=update.chat.id,
        text=Translation.START_TEXT.format(update.from_user.mention),
        parse_mode="html", disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton('⚙ Channel ⚙', url='https://telegram.me/FayasNoushad'), InlineKeyboardButton('⚙ Group ⚙', url='https://telegram.me/FayasChat')]]),
        reply_to_message_id=update.message_id
    )
