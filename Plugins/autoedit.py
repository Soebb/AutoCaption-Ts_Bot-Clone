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


@autocaption.on_message(~filters.edited, group=-1)
async def editing(bot, message):
    if (message.chat.type == "private"):
        if ("/set_cap" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 𝐂𝐀𝐏𝐓𝐈𝐎𝐍 \n\nUse this command to set custom caption for any of your channels.\n\n👉 `/set_cap -1001448973320 My Caption`", quote = True)
        elif ("/set_cap" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            caption = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "")
            try:
                await update_caption(channel, caption)
            except Exception as e:
                print(e)
                return await message.reply_text("⚠️\n\nIt seems a caption already seted for this channel id, you should first use /rmv_cap command to remove the current caption and then try seting new again.", quote=True)
            await message.reply_text(f"**--Your Caption--:**\n\n{caption}", quote=True)
        if ("/set_btn" in message.text) and ((len(message.text.split(' ')) == 2) or (len(message.text.split(' ')) == 1)):
            await message.reply_text("🖊️ 𝐒𝐄𝐓 BUTTON \n\nUse this command to set button for any of your channels.\nSend a Button name and URL(separated by ' | ').\n\n👉 `/set_btn -1001448973320 Channel | https://t.me/channel`", quote = True)
        elif ("/set_btn" in message.text) and (len(message.text.split(' ')) != 2) and (len(message.text.split(' ')) != 1):
            button = message.text.split(' ', 2)[2]
            channel = message.text.split(' ', 2)[1].replace("-100", "").replace("1", "")
            try:
                await update_button(channel, button)
            except Exception as e:
                print(e)
                return await message.reply_text("⚠️\n\nIt seems a button already seted for this channel id.\nYou should first use /rmv_btn command to remove the current button and then try to seting new.", quote=True)
            await message.reply_text(f"**--Your Button--:**\n\n{button}", quote=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(button.split(' | ')[0], url=f"{button.rsplit(' ', 1)[1]}")]]))
      
        if (message.text == "/rmv_cap"):
            await message.reply_text("Use this command to remove the current caption of any of your channels.\n\n👉 `/rmv_cap -1001448973320`", quote = True)
        elif ("/rmv_cap" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "")
            await del_caption(channel)
            await message.reply_text("✅The Caption Removed Successfully.", quote=True)
        if (message.text == "/rmv_btn"):
            await message.reply_text("Use this command to remove the current button of any of your channels.\n\n👉 `/rmv_btn -1001448973320`", quote = True)
        elif ("/rmv_btn" in message.text) and (len(message.text.split(' ')) != 1):
            channel = message.text.split(' ', 1)[1].replace("-100", "").replace("1", "")
            await del_button(channel)
            await message.reply_text("✅The Button Removed Successfully.", quote=True)

    if (message.chat.type == "channel"):
        media = message.video or message.document or message.audio
        try:
            channel = str(message.chat.id).replace('-100', '').replace('1', '')
            btn = await get_button(int(channel))
            button = btn.button
        except Exception as e:
            button = None
            print(f"eror: {e}")
            pass

        try:
            channel = str(message.chat.id).replace('-100', '')
            cap = await get_caption(int(channel))
            caption = cap.caption.replace("fname", f"{media.file_name}")
        except:
            caption = " "
            pass
       
        if button is not None:
            Url = button.rsplit(' ', 1)[1]
            Name = button.split(' | ')[0]
            try:
                await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = f'{caption}', parse_mode = "markdown", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(Name, url=f"{Url}")]]))
            except Exception as e:
                print(e)

        elif button is None:
            try:
                await bot.edit_message_caption(chat_id = message.chat.id, message_id = message.message_id, caption = f'{caption}', parse_mode = "markdown")
            except Exception as e:
                print(e)

        '''if key and poster:
            await message.reply_photo(photo=poster, caption=
            await msg.copy(message.chat.id)
            await msg.delete()'''
      
