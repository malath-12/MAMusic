import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›"," ","السورس"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://graph.org/file/68a6ad87680189beb51b8.jpg",
        caption = f"""<b>  ⌯ 𝐰𝐞𝐥𝐜𝐨𝐦𝐞 𝐭𝐨 . .<b>\n<a href="https://t.me/sourcerona"> 𝐬𝐨𝐮𝐫𝐜𝐞 𝐫𝐨𝐧𝐚</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "المطور", url=f"https://t.me/R_J_y"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "𝐬𝐨𝐮𝐫𝐬 𝐫𝐨𝐧𝐚", url=f"https://t.me/sourcerona"),         
                ],

            ]

        ),

    )
