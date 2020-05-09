# Scrapping images from the internet:

import requests
from bs4 import BeautifulSoup as bs
import os

# url with modelimages
url = 'https://'

# download page for parsing
page = requests.get(url)
soup = bs(page.text, 'html.parser')

# locate all elements with image tag
image_tags = soup.findAll('img')

# create the directory we want to store images in
if not os.path.exists('models'):
    os.makedirs('models')

os.chdir('models')

# move to new directory
os.chdir('models')

#image file name variable
x = 0

# writing images
for image in image_tags:
    try:
        url = image['src']
        source = requests.get(url)
        if source.status_code == 200:
            with open('model-' + str(x) + '.jpg', 'wb') as f:
                f.write(requests.get(url).content)
                f.close()
                x += 1
    except:
        pass


# The Model Bot:

import tweepy as tp
import time
import os

# credentials to log in to twitter api
consumrer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

# log in twitter account api
auth = tp.OAuthHandler(consumrer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

#iterates over images in models folder
os.chdir('models')
for model_image in os.listdir(','):
    api.update_with_media(model_image)
    time.sleep(5)       # in sec