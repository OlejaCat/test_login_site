import telegram
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CallbackContext, CommandHandler, MessageHandler, filters
from config import TOKEN
import json


async def launch_web_ui(update: Update, callback: CallbackContext):
    await update.effective_chat.send_message("I hear you loud and clear !")


async def launch_web_ui(update: Update, callback: CallbackContext):
    kb = [
        [KeyboardButton("Show me Google!", web_app=WebAppInfo("https://google.com"))]
    ]
    await update.message.reply_text("Let's do this...", reply_markup=ReplyKeyboardMarkup(kb))


if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', launch_web_ui))

    print(f"Your bot is listening! Navigate to http://t.me/nope to interact with it!")
    application.run_polling()
