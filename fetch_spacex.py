import os
import requests
from random import shuffle
from urllib.parse import urlsplit, unquote


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
