import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config
from database.database import *


@autocaption.on_message(~filters.edited, group=-1)
async def editing(bot, message):
    if (message.chat.type == "private") and (message.text.startswith("/set")):
        if (message.text == "/set") or (len(message.text.split(' ')) == 2):
            await
        else:
            await
        caption = cmd.text.split(' ', 1)
        await update_caption(cmd.from_user.id, caption)
        await cmd.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)

    cap = await get_caption(message.from_user.id)
    try:
        caption = cap.caption.replace("fname", f"{message.media.file_name}")
    except Exception as e:
        print(e)
        caption = message.caption
        pass
      
    msg = await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = f'{caption}', parse_mode = "markdown")
    '''if key and poster:
          await message.reply_photo(photo=poster, caption=
          await msg.copy(message.chat.id)
          await msg.delete()'''
      
                   
      
