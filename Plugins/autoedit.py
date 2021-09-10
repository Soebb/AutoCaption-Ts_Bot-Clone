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
    if (message.chat.type == "private") and ("/set" in message.text):
        if (message.text == "/set") or (len(message.text.split(' ')) == 2):
            await message.reply_text(
            "🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set your own caption text \n\n👉 `set_caption My Caption`", 
            quote = True
            )
        else:
            caption = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "")
            await update_caption(channel, caption)
            await message.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)
    if (message.chat.type == "channel"):
        try:
            cap = await get_caption(message.chat.id.replace('-100', ''))
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
      
                   
  
