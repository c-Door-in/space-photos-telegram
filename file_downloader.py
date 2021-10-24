import os
import requests
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
