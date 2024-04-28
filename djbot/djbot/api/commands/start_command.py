import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext


async def handle_message(update: Update, context: CallbackContext) -> None:
    user_text = update.message.text
    chat_id = update.message.chat_id
    response_text = f"You said: {user_text}"
    await context.bot.send_message(chat_id=chat_id, text=response_text)


def main():
    application = Application.builder().token(os.environ.get('BOT_TOKEN')).build()

    text_handler = MessageHandler(filters.TEXT, handle_message)
    application.add_handler(text_handler)

    application.run_polling()
