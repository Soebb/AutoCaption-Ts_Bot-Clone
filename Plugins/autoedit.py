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
    if (message.chat.type == "private"):
        if ("/set" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set your own custom caption for any of your channels.\n\n👉 `/set -1001448973320 My Caption`", quote = True)
        elif ("/set" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            caption = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "")
            try:
                await update_caption(channel, caption)
            except Exception as e:
                print(e)
                return await message.reply_text("It seems you already seted caption for that channel id, you should first use /rmv command to remove the current caption and then try seting new again.")
        if (message.text == "/rmv"):
            await message.reply_text("Use this command to remove the current caption of any of your channels.\n\n👉 `/rmv -1001448973320`", quote = True)
        elif ("/rmv" in message.text) and (len(message.text.split(' ')) != 1):
            await del_caption(channel)
            await message.reply_text("The seted caption removed successfully.")

    if (message.chat.type == "channel"):
        media = message.video or message.document or message.audio
        channel = str(message.chat.id).replace('-100', '')
        try:
            cap = await get_caption(int(channel))
            caption = cap.caption.replace("fname", f"{media.file_name}")
        except Exception as e:
            print(e)
            caption = message.caption
            pass
      
        msg = await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = f'{caption}', parse_mode = "markdown")
        '''if key and poster:
            await message.reply_photo(photo=poster, caption=
            await msg.copy(message.chat.id)
            await msg.delete()'''
      
                   
  
