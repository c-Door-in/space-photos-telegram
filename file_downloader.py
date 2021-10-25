import os
import requests
from urllib.parse import urlsplit, unquote



def parse_url_file_ext(url):
    path = unquote(urlsplit(url).path)
    filename = os.path.basename(path)
    return os.path.splitext(filename)[1]


def download_image(url, local_image_path):
    response = requests.get(url)
    response.raise_for_status()
    ext = parse_url_file_ext(url)
    with open(f'{local_image_path}{ext}', 'wb') as file:
        return file.write(response.content)
