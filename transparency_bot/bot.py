from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import requests
import logging
from . import img
token = open('token.txt', 'r').read().rstrip()
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
whitelist = ['idmyn']


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="I'm a bot, please talk to me!")


def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text=update.message.text)


def image(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="nice pic")

    if update.effective_chat.username not in whitelist:
        return  # I don't want to process images from strangers

    biggestImage = max(update.message.photo, key=lambda x:x['file_size'])
    # ^ https://stackoverflow.com/a/5326622/10314380
    file_id = biggestImage.file_id

    file_path_url = 'https://api.telegram.org/bot{0}/getFile?file_id={1}'.format(token, file_id)
    r = requests.get(file_path_url)
    file_path = r.json()['result']['file_path']
    file_url = 'https://api.telegram.org/file/bot{0}/{1}'.format(token, file_path)
    image = requests.get(file_url)

    bytes = img.white_to_transparent(image.content)
    bytes.name = "img.png"
    bytes.seek(0)
    context.bot.send_document(chat_id=update.effective_chat.id,
                              document=bytes)


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
