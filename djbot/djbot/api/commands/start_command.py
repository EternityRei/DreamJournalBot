import os

from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
from djbot.core.agent import Agent


async def handle_message(
        update: Update,
        context: CallbackContext,
        agent: Agent
) -> None:
    user_text = update.message.text
    chat_id = update.message.chat_id
    agent_response = agent.ask(user_text)['output']
    await context.bot.send_message(chat_id=chat_id, text=agent_response)


def main():
    application = Application.builder().token(os.environ.get('BOT_TOKEN')).build()

    agent = Agent()

    text_handler = MessageHandler(filters.TEXT, lambda update, context: handle_message(update, context, agent))
    application.add_handler(text_handler)

    application.run_polling()
