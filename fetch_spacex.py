import os
import requests
from random import shuffle

from environs import Env

from file_downloader import download_image


def parse_spacex_random_launch_images():
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
    launch_images = parse_spacex_random_launch_images()
    if launch_images:
        local_path = f'{images_directory}/spacex'
        os.makedirs(local_path, exist_ok=True)
        for image_id, image_url in enumerate(launch_images):
            local_image_path = f'{local_path}/spacex_{image_id}'
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
