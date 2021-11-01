import os
from datetime import datetime

import requests
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


def fetch_nasa_apod_images(api_key, images_directory, image_count=''):
    all_apod_images = parse_nasa_apod_images(api_key, image_count)
    local_path = f'{images_directory}/nasa_apod'
    os.makedirs(local_path, exist_ok=True)
    for image_id, image_details in enumerate(all_apod_images):
        is_hd_image = 'hdurl' in image_details
        url = image_details['hdurl'] if is_hd_image else image_details['url']
        local_image_path = f'{local_path}/nasa_apod_{image_id}'
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
    all_epic_images = parse_nasa_epic_images(api_key)
    local_path = f'{images_directory}/nasa_epic'
    os.makedirs(local_path, exist_ok=True)
    for image_id, epic_image_details in enumerate(all_epic_images):
        url = get_epic_image_url(epic_image_details)
        local_image_path = f'{local_path}/nasa_epic_{image_id}'
        params = {'api_key': api_key}
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
