from telegram.ext import Updater, CommandHandler
token = open('token.txt', 'r').read().rstrip()


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")


def run():
    print("running...")

    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
