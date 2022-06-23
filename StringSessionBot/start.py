from Data import Data
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup


# Start Message
@Client.on_message(filters.text & filters.private & filters.command("start"))
async def start(bot, msg):
    user = await bot.get_me()
    mention = user["mention"]
    await bot.send_message(
        msg.chat.id,
        Data.START.format(msg.from_user.mention, mention),
        reply_markup=InlineKeyboardMarkup(Data.buttons)
    )
