import telegram
import time
from os import listdir

from environs import Env


def upload_photo(bot, chat_id, period):
    for dir in listdir('images'):
        for file in listdir(f'images/{dir}'):
            bot.send_photo(chat_id=chat_id, photo=open(f'images/{dir}/{file}', 'rb'))
            time.sleep(period)


def main():
    env = Env()
    env.read_env()
    bot = telegram.Bot(token=env('TG_TOKEN'))
    chat_id = '@spimg'
    upload_photo(bot, chat_id, env.int('PUBLIC_PERIOD', default=86400))


if __name__ == '__main__':
    main()