import requests
import os


os.makedirs('images', exist_ok=True)

def download_image(url, image_name):
    response = requests.get(url)
    response.raise_for_status()
    response.json
    with open(f'images/{image_name}', 'wb') as file:
        return file.write(response.content)


def get_spacex_images_path(flight_id):
    spacex_api_url = f'https://api.spacexdata.com/v4/launches/{flight_id}'
    response = requests.get(spacex_api_url)
    response.raise_for_status()
    return response.json()['links']['flickr']['original']


def fetch_spacex_one_launch():
    flight_id = '5fe3b11eb3467846b324216c'
    for image_id, spacex_image_url in enumerate(get_spacex_images_path(flight_id)):
        image_name = f'space{image_id}.jpeg'
        download_image(spacex_image_url, image_name)


def main():
    fetch_spacex_one_launch()


if __name__ == '__main__':
    main()