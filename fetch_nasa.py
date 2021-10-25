import requests
import os
from datetime import datetime

from environs import Env

from file_downloader import download_image


def parse_nasa_apod_images(api_key, image_count):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': api_key,
        'count': image_count
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()


def get_better_image(image_details):
    is_hd_image = 'hdurl' in image_details
    return image_details['hdurl'] if is_hd_image else image_details['url']


def fetch_nasa_apod_images(api_key, images_directory, image_count=''):
    all_apod_info = parse_nasa_apod_images(api_key, image_count)
    for image_id, apod_image_details in enumerate(all_apod_info):
        url = get_better_image(apod_image_details)
        local_image_path = f'{images_directory}/nasa_apod/nasa_apod_{image_id}'
        os.makedirs(os.path.dirname(local_image_path), exist_ok=True)
        download_image(url, local_image_path)
    return


def parse_nasa_epic_images(api_key):
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


def get_epic_image_url(image_details):
    src_image_name = image_details['image']
    src_image_date = format_url_image_date(image_details['date'])
    return (
        'https://api.nasa.gov/EPIC/archive/natural/'
        f'{src_image_date}/png/{src_image_name}.png'
    )


def fetch_nasa_epic_images(api_key, images_directory):
    for image_id, epic_image_details in enumerate(parse_nasa_epic_images(api_key)):
        url = get_epic_image_url(epic_image_details)
        params = {'api_key': api_key}
        local_image_path = f'{images_directory}/nasa_epic/nasa_epic_{image_id}'
        os.makedirs(os.path.dirname(local_image_path), exist_ok=True)
        download_image(url, local_image_path, params=params)


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
    