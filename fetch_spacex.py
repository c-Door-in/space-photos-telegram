import os
import requests
from random import shuffle

from file_downloader import download_image


def parse_spacex():
    spacex_api_url = f'https://api.spacexdata.com/v4/launches'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    for flight_obj in shuffle(response.json()):
        if flight_obj['links']['flickr']['original']:
            return flight_obj['links']['flickr']['original']
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
