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
        photo=f"https://graph.org/file/d26a24c11bd88d3bd305a.jpg",
        caption = f"""<b>𝘄𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 . .<b>\n<a href="https://t.me/sourcerona"> 𝘀𝗼𝘂𝗿𝗰𝗲 𝗹𝗶𝘀𝗮</a></b>""",
reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "• 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 Raneem", url=f"https://t.me/R_J_y"),
                ],[
                    
                
                    InlineKeyboardButton(
                        "𝘀𝗼𝘂𝗿𝗰𝗲 Raneem", url=f"https://t.me/sourcerona"),         
                ],

            ]

        ),

    )
