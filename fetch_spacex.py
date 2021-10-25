import os
import requests
from random import shuffle

from environs import Env

from file_downloader import download_image


def parse_spacex():
    spacex_api_url = f'https://api.spacexdata.com/v4/launches'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    all_spacex_launches = response.json()
    shuffle(all_spacex_launches)
    for launch in all_spacex_launches:
        if launch['links']['flickr']['original']:
            return launch['links']['flickr']['original']
    return


def fetch_spacex_launch_images(images_directory):
    for image_id, image_url in enumerate(parse_spacex()):
        local_image_path = f'{images_directory}/spacex/spacex_{image_id}'
        os.makedirs(os.path.dirname(local_image_path), exist_ok=True)
        download_image(image_url, local_image_path)
    return


def main():
    env = Env()
    env.read_env()
    images_directory = env('LOCAL_IMAGES_DIR', default='images')
    os.makedirs(images_directory, exist_ok=True)
    fetch_spacex_launch_images(images_directory)


if __name__ == '__main__':
    main()
