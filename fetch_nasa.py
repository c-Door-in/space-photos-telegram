import requests
import os
from datetime import datetime

from environs import Env

from file_downloader import download_image


def parse_nasa_apod(api_key, image_count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': image_count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def fetch_nasa_apod_images(api_key, images_directory, image_count=''):
    for image_id, res_obj in enumerate(parse_nasa_apod(api_key, image_count)):
        src_name = 'nasa_apod'
        image_name = f'{src_name}_{image_id}'
        if 'hdurl' in res_obj:
            url = res_obj['hdurl']
        else:
            url = res_obj['url']
        download_image(url, src_name, images_directory, image_name)
    return


def parse_nasa_epic(api_key):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': api_key,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def format_url_image_date(src_image_date):
    image_date = datetime.fromisoformat(src_image_date)
    return image_date.date().strftime('%Y/%m/%d')


def get_image_url_from_epic_object(api_key, image_obj):
    src_image_name = image_obj['image']
    src_image_date = format_url_image_date(image_obj['date'])
    return (
        'https://api.nasa.gov/EPIC/archive/natural/'
        f'{src_image_date}/png/{src_image_name}.png'
        f'?api_key={api_key}'
    )


def fetch_nasa_epic_images(api_key, images_directory):
    for image_id, image_obj in enumerate(parse_nasa_epic(api_key)):
        url = get_image_url_from_epic_object(api_key, image_obj)
        local_image_path = f'{images_directory}/nasa_epic/nasa_epic_{image_id}'
        os.makedirs(os.path.dirname(local_image_path), exist_ok=True)
        download_image(url, local_image_path)


def main():
    env = Env()
    env.read_env()
    api_key = env('NASA_API_KEY', default='DEMO_KEY')
    images_directory = env('LOCAL_IMAGES_DIR', default='images')
    os.makedirs(images_directory, exist_ok=True)
    fetch_nasa_apod_images(api_key, images_directory, image_count='30')
    fetch_nasa_epic_images(api_key, images_directory)


if __name__ == '__main__':
    main()
    