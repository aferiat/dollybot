"""
Simple Bot to reply to Telegram messages taken from the python-telegram-bot examples.
Deployed using heroku.
Author: liuhh02 https://medium.com/@liuhh02
"""

from dotenv import load_dotenv
import os
from pathlib import Path
import random
import time
import codecs
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
#PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '2065367783:AAHKgUvA_8aoQn6QG6DIQTfSqAtsWrYzICc'

''' Windows Path to songs '''
#PATH=Path("C:/Users\WEARY\Desktop\Dolly")

''' aws Path to songs '''

PATH=Path("/home/dolly")


chat_id = set()
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /dolly is issued."""
    global chat_id
    update.message.reply_text('Taaachhh')
    chat_id.add(update.message.chat.id)
    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('khask tkon sa3oudi la khassk mosa3ada')

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def bar(context: CallbackContext):
    """Sends a bar from Dolly."""
    job = context.job
    global chat_id
    ''' LOAD SONGS '''
    filename =[]
    for f in PATH.iterdir():
        filename.append(f.name)

    ''' Choose random song '''
    f= random.choice(filename)
    print("Song : " + f[:-4])
    #f = open(PATH/f, "r")
    f = codecs.open(PATH/f, "r", encoding='utf-8')
    lines = f.readlines()
    #print(lines)
    line = random.choice(lines)
    ''' Choose random bar '''
    while line[0]=='[' or (line in ['\n', '\r\n']):
        line = random.choice(lines)
    print("bar : " + line.rstrip())
    f.close()
    #update.message.reply_text(line.rstrip())
    for c in chat_id:
        context.bot.send_message(chat_id=c, text=line.rstrip())



def bar1(update, context):
    """Sends a bar from Dolly."""
    global chat_id
    ''' LOAD SONGS '''
    filename =[]
    for f in PATH.iterdir():
        filename.append(f.name)

    ''' Choose random song '''
    f= random.choice(filename)
    print("Song : " + f[:-4])
    #f = open(PATH/f, "r")
    f = codecs.open(PATH/f, "r", encoding='utf-8')
    lines = f.readlines()
    #print(lines)
    line = random.choice(lines)
    ''' Choose random bar '''
    while line[0]=='[' or (line in ['\n', '\r\n']):
        line = random.choice(lines)
    print("bar : " + line.rstrip())
    f.close()
    update.message.reply_text(line.rstrip())
    # for c in chat_id:
    #     context.bot.send_message(chat_id=c, text=line.rstrip())

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)
    j = updater.job_queue
    
    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("dolly", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("ster", bar1))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))
    #dp.add_handler(MessageHandler(Filters.text, bar))
    job_minute = j.run_repeating(bar, interval=3600, first=10)
    # log all errors
    dp.add_error_handler(error)
    
    # Start the Bot
    updater.start_polling()
    
    # # Start the Bot
    # updater.start_webhook(listen="0.0.0.0",
    #                       port=int(PORT),
    #                       url_path=TOKEN)
    # updater.bot.setWebhook('https://yourherokuappname.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()