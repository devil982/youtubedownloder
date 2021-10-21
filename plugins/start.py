from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/pranthan_321")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b><b> i am a youtube downloader bot</b>\n/help for More info"
                                  
    await message.reply_photo("https://telegra.ph/file/a93dd72c108a2ff0342fd.jpg")
    message.reply_text("hi.. i am a youtube downloaderbot")
     
    raise StopPropagation
