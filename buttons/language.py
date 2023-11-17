from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ContextTypes, CallbackContext

from buttons.templates import say_lang
from db.MySqlConn import Mysql
from config import CHOOSING


async def show_languages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("Русский", callback_data='lang_ru'),
            InlineKeyboardButton("English", callback_data='lang_en'),
            InlineKeyboardButton("中文", callback_data='lang_cn'),
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Please choose your language:', reply_markup=reply_markup)
    return CHOOSING


async def show_languages_callback_handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.callback_query.from_user.id

    query = update.callback_query
    # CallbackQueries need to be answered, even if no notification to the user is needed
    await query.answer()

    user_id = update.effective_user.id
    lang = query.data.split("_")[1]
    mysql = Mysql()
    mysql.update("update users set lang=%s where user_id=%s", (lang, user_id))
    mysql.end()

    await query.edit_message_text(say_lang[lang])
