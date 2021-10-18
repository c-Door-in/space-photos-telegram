import requests
import os


os.makedirs('images', exist_ok=True)

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
response = requests.get(url)

with open('images/hubble.jpeg', 'wb') as file:
    file.write(response.content)