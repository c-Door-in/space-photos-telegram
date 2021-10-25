# Space Photos Telegram
This project allows you to download space photos from SpaceX and NASA api resources, and post them automatically to your Telegram channel.

You can set the time delay for posting the next photo.
The service uses:
- SpaceX launches images from [api.spacexdata.com](https://github.com/r-spacex/SpaceX-API/blob/master/docs/launches/v4/all.md)
- NASA Astronomy Picture of the Day (APOD) and Earth Polychromatic Imaging Camera (EPIC) from [api.nasa.gov](https://api.nasa.gov/)

# How to install
## Install requirements

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
## Create your own Telegram bot
Create a bot by using instructions of `@botfather` in Telegram.
Copy `TOKEN` that @botfather give you. 
Make the bot the administrator of your Telegram channel.
## Prepare virtual environment
Create `.env` file in the root and place necessary data in there.
- Get NASA `api key` from [api.nasa.gov](https://api.nasa.gov/).

*By default, there is a token `DEMO_KEY` in the program. But it has limited opportunities.*
```
NASA_API_KEY=[your nasa api key]
```
- Put your Telegram bot `TOKEN`.
```
TG_TOKEN=[your telegram bot token]
```
- Put your Telegram channel `chat_id`.
```
CHAT_ID=[@your_channel_chat_id]
```
- You can change the delay your bot uses before posting the next image. By default, this is the hour. Specify new in seconds.
```
PUBLISH_PERIOD=[any delay value in seconds]
```

# How to start
- Get new SpaceX photos with
```
python fetch_spacex.py
```
- Get new NASA photos with
```
python fetch_nasa.py
```
- Launch publish service
```
python publish_photo.py
```

# Project Goals
The code is written for educational purposes on online-course for web-developers [dvmn.org](https://www.dvmn.org).
