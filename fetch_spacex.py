import requests
import os
from datetime import datetime
from urllib.parse import urlsplit, unquote

from environs import Env


def parse_url_file_ext(url):
    path = unquote(urlsplit(url).path)
    filename = os.path.basename(path)
    return os.path.splitext(filename)[1]


def download_image(url, src_name, image_name):
    response = requests.get(url)
    response.raise_for_status()
    ext = parse_url_file_ext(url)
    os.makedirs(f'images/{src_name}', exist_ok=True)
    with open(f'images/{src_name}/{image_name}{ext}', 'wb') as file:
        return file.write(response.content)


def parse_spacex(flight_id):
    spacex_api_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    return response.json()


def fetch_spacex_one_launch_images(flight_id):
    images_url_list = parse_spacex(flight_id)['links']['flickr']['original']
    for image_id, image_url in enumerate(images_url_list):
        src_name = 'space'
        image_name = f'{src_name}_{image_id}'
        download_image(image_url, src_name, image_name)
    return


def main():
    env = Env()
    env.read_env()
    spacex_flight_id = env('SPACEX_FLIGHT_ID')

    os.makedirs('images', exist_ok=True)
    fetch_spacex_one_launch_images(spacex_flight_id)


if __name__ == '__main__':
    main()