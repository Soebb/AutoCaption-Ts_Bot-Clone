import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config
from database.database import *


# =
usercaption_position = Config.CAPTION_POSITION
caption_position = usercaption_position.lower()


@autocaption.on_message(filters.channel & (filters.document | filters.video | filters.audio ) & ~filters.edited, group=-1)
async def editing(bot, message):
    cap = await get_caption()
    try:
        caption = cap.caption.replace("fname", "{message.media.file_name}")
    except:
        caption = message.caption
        pass
      
    msg = await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = f'{caption}', parse_mode = "markdown")
    '''if key and poster:
          await message.reply_photo(photo=poster, caption=
          await msg.copy(message.chat.id)
          await msg.delete()'''
      
                   
      
