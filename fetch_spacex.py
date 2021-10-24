import os
import requests
from random import shuffle

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


def fetch_spacex_launch_images():
    for image_id, image_url in enumerate(parse_spacex()):
        src_name = 'spacex'
        image_name = f'{src_name}_{image_id}'
        download_image(image_url, src_name, image_name)
    return


def main():
    os.makedirs('images', exist_ok=True)
    fetch_spacex_launch_images()


if __name__ == '__main__':
    main()