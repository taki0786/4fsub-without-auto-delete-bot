#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ OWNER : <a href='t./me/Urr_Sanjii'>This Person</a>\n<b>○ Anime Channel : <a href='t./me/SAGATO_ANIME'>Sagato Anime</a>\n <b>○ Anime Movies : <a href='t./me/sagato_anime_movies'>Sagato Movies</a>\n○ Language : <code>Python3</code>\n○ 👨‍💻 Creator : @Urr_Sanji </b>",
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
