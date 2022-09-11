from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_ID = "15530355"
API_HASH = "4ca71076aff9fb546651db89c9cae8b1"
BOT_TOKEN = "5691093159:AAFORC2hJdHJfPW5P88QFSChFvNr0n-a6pM"


RMMODS = Client(
    name="18---Bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN
) 

START_BUTTONS = [[
  InlineKeyboardButton("group", url="https://t.me/+o-MQ_xH-KOk2OWZl"),
  InlineKeyboardButton("channel", url="https://t.me/+sWoGaitW8200OGI9")
  ]]


@RMMODS.on_message(filters.command("start")) 
async def start_cmd(client, message):
    await message.reply_photo(
        photo="https://telegra.ph/file/ae8ba6d9bc7b00e7346ce.jpg", 
        caption="Hey Iam pyrogram Bot",
         reply_markup=InlineKeyboardMarkup(START_BUTTONS) 
    ) 

@RMMODS.on_message(filters.command("about")) 
async def about_cmd(client, message):
    await message.reply_text("Bot Status")    




print("Bot Was Started")

RMMODS.run() 
