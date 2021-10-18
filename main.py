import requests
import os


os.makedirs('images', exist_ok=True)

def download_image(url, image_name):
    response = requests.get(url)
    response.raise_for_status()
    with open(f'images/{image_name}', 'wb') as file:
        file.write(response.content)


def main():
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
    name = 'hubble.jpeg'
    download_image(url, name)


if __name__ == '__main__':
    main()