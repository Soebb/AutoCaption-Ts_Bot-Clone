import logging
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

import asyncio
from pyrogram import filters
from bot import autocaption
from config import Config
from database.database import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import FloodWait
import re

F = "a b button name × https gh"
print(re.split(r"[×\s]", F, maxsplit=3))
print(re.split('[× \\s]', F, maxsplit=3))
print(re.split('[× \\s+]', F, maxsplit=3))
print(re.split('[None x]', F, maxsplit=3))


@autocaption.on_message(~filters.edited, group=-1)
async def editing(bot, message):
    if (message.chat.type == "private"):
        if ("/set_cap" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set your own custom caption for any of your channels.\n\n👉 `/set_cap -1001448973320 My Caption`", quote = True)
        elif ("/set_cap" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            caption = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "")
            try:
                await update_caption(channel, caption)
            except Exception as e:
                print(e)
                return await message.reply_text("It seems you already seted caption for that channel id, you should first use /rmv_cap command to remove the current caption and then try seting new again.")
            await message.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)
        if ("/set_btn" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set your own button for any of your channels.\nSend a Button name and URL separated by ' | '\n\n👉 `/set_btn -1001448973320 Button Name | https://t.me/my_channel`", quote = True)
        elif ("/set_btn" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            button = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-", "")
            try:
                await update_button(channel, button)
            except Exception as e:
                print(e)
                return await message.reply_text("It seems you already seted button for that channel id, you should first use /rmv_btn command to remove the current button and then try seting new again.")
            await message.reply_text(f"**--Your Button--:**\n\n{button}", quote=True)
      
        if (message.text == "/rmv_cap"):
            await message.reply_text("Use this command to remove the current caption of any of your channels.\n\n👉 `/rmv_cap -1001448973320`", quote = True)
        elif ("/rmv_cap" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "")
            await del_caption(channel)
            await message.reply_text("The Caption Removed Successfully.")
        if (message.text == "/rmv_btn"):
            await message.reply_text("Use this command to remove the current button(s) of any of your channels.\n\n👉 `/rmv_btn -1001448973320`", quote = True)
        elif ("/rmv_btn" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-", "")
            await del_button(channel)
            await message.reply_text("The Button Removed Successfully.")

    
