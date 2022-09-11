from pyrogram import Client, filters


API_ID = "15530355"
API_HASH = "4ca71076aff9fb546651db89c9cae8b1"
BOT_TOKEN = "5691093159:AAFORC2hJdHJfPW5P88QFSChFvNr0n-a6pM"


RMMODS = Client(
    name="18---Bot", 
    api_id=API_ID, 
    api_hash=API_HASH, 
    bot_token=BOT_TOKEN
) 



@RMMODS.on_message(filters.command("start")) 
async def start_cmd(client, message):
    print("START Command")

@RMMODS.on_message(filters.command("help")) 
async def help_cmd(client, message):
    print("HELP Command")




print("Bot Was Started")

RMMODS.run() 
