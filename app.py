from telebot import TeleBot
from dotenv import load_dotenv
from datetime import datetime
import os


load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')


bot = TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")


def responses(message):
    if message.lower() in ('hi', 'hello', 'how are you'):
        return 'Hello! How are you?'
    if message.lower() == 'what date is today?':
        now = datetime.now()
        return f'today is {now.day}-{now.month}-{now.year} : {now.hour}:{now.minute}'
    return 'Sorry, I cant understand you'


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    res = responses(message.text)
    bot.reply_to(message, res)


def main():
    bot.polling()


if __name__ == '__main__':
    main()