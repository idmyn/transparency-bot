from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
token = open('token.txt', 'r').read().rstrip()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)


def image(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="nice pic")

def run():
    print("running...")

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    echo_handler = MessageHandler(Filters.text, echo)
    dispatcher.add_handler(echo_handler)

    image_handler = MessageHandler(Filters.photo, image)
    dispatcher.add_handler(image_handler)


    updater.start_polling()
    updater.idle()
