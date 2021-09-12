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
from datetime import datetime, timedelta
from threading import Timer

F = "a -10 button name | https"

Url = F.rsplit(' ', 1)[1]
Name = F.split(' ', 2)[2].replace(f" | {Url}", "")
print(Url)
print(Name)

x=datetime.today()
y=x.replace(day=x.day, hour=x.hour, minute=x.minute+4, second=x.second, microsecond=x.microsecond)
delta_t=y-x

secs=delta_t.seconds+1
@autocaption.on_message(~filters.edited, group=-1)
async def editing(bot, update):
   await bot.send_message(chat_id = -1001264182630, text = "a")


t = Timer(secs, editing)
t.start()
