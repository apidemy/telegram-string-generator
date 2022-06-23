from Data import Data
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, Message


# Get Chat ID
@Client.on_message(filters.forwarded & filters.private & filters.incoming & (filters.text | filters.media) & ~filters.edited)
async def get_chat_id(bot: Client, msg: Message):
    if msg.forward_from_chat and msg.forward_from_chat.type == 'channel':
        text_str = 'Forward Detected\n\n' + \
            msg.forward_from_chat.type + '\n' + \
            '`' + msg.forward_from_chat.title + '`\n' + \
            '@' + msg.forward_from_chat.username + '\n' + \
            'id: `' + str(msg.forward_from_chat.id) + '`\n'
        await bot.send_message(
            msg.chat.id,
            text_str,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(Data.home_buttons),
        )
