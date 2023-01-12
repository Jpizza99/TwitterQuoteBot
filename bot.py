import tweepy
import requests
import time
import random



#Quotable Setup
QUOTABLE_URL = 'https://api.quotable.io/random'

while True:
  QuoteJSON = requests.get(QUOTABLE_URL).json()
  quote = QuoteJSON['content'] + ' -' + QuoteJSON['author']
  
  #Test
  print(quote)

  
  auth = tweepy.OAuth1UserHandler(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
  api = tweepy.API(auth)
  media = api.media_upload('images\\BG'+str(random.randint(1,16)) + '.png')

  api.update_status(quote, media_ids=[media.media_id])
  time.sleep(1500)