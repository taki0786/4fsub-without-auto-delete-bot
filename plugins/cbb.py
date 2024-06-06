# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper




from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery



@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 My Father :</b> <a href='https://t.me/Urr_Sanjii'> Sanjii Sama</a> \n<b>Anime Series :</b> <a href='https://t.me/sagato_anime'> ՏᎪᏀᎪͲϴ ᎪΝᏆᎷᎬ</a></b> \n<b>Anime Movies :</b> <a href='https://t.me/sagato_anime_Movies'> ՏᎪᏀᎪͲϴ ᎪΝᏆᎷᎬ ᗰOᐯIᗴՏ </a></b> \n<b>Chat Group :</b> <a href='https://t.me/apna_akatsuki'> ☁️ ᴀᴋᴀᴛsᴜᴋɪ ☁️ </a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
