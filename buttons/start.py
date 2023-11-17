from telegram import Update
from telegram.ext import ContextTypes
from buttons.templates import start_responce
import time

from config import (
    reply_markup,
    CHOOSING)
from db.MySqlConn import Mysql


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    mysql = Mysql()
    user = update.effective_user
    user_id = user.id

    user_checkin = mysql.getOne(f"select * from users where user_id={user_id}")
    if not user_checkin:
        date_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = "insert into users (user_id, name, level, system_content, created_at) values (%s, %s, %s, %s, %s)"
        value = [user_id, user.username, 0, "You are an AI assistant that helps people find information.", date_time]
        mysql.insertOne(sql, value)
    mysql.end()

    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_text(start_responce[user_checkin["lang"]])

    return CHOOSING
