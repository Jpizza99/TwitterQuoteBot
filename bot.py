import tweepy
from tweepy import OAuthHandler
import requests
import time
import random


IMAGE_COUNT = 32




#Quotable Setup
QUOTABLE_URL = 'https://api.quotable.io/random'
x = []

for i in range(1, IMAGE_COUNT+1):
  x.append(i) 

while True:
  QuoteJSON = requests.get(QUOTABLE_URL).json()
  quote = QuoteJSON['content'] + ' -' + QuoteJSON['author']
  
  #Test
  print(quote)

  
  auth = OAuthHandler(API_KEY, API_KEY_SECRET)
  auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)


  if(len(x) != 0):
    image = x.pop(random.randint(0,len(x)-1))
  else:
    for i in range(1, IMAGE_COUNT+1):
      x.append(i) 
  
  media = api.media_upload('images/BG'+str(image) + '.png')

  api.update_status(quote, media_ids=[media.media_id])
  time.sleep(1500)
