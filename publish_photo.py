import time
from os import listdir

import telegram
from environs import Env


def upload_photo(bot, chat_id, images_directory, period):
    for dir in listdir(images_directory):
        for file in listdir(f'{images_directory}/{dir}'):
            with open(f'{images_directory}/{dir}/{file}', 'rb') as photo:
                bot.send_photo(
                    chat_id=chat_id,
                    photo=photo
                )
            time.sleep(period)


def main():
    env = Env()
    env.read_env()
    upload_photo(
        telegram.Bot(token=env('TG_TOKEN')),
        env('CHAT_ID'),
        env('LOCAL_IMAGES_DIR', default='images'),
        env.int('PUBLISH_PERIOD', default=86400)
    )


if __name__ == '__main__':
    main()
