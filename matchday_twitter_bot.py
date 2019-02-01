#!/usr/bin/env python3

import tweepy

print("Hello! I am a twitter bot")

CONSUMER_API_KEY 	= "axZ2zerBvFN3LNiDtguq78Kc4"
CONSUMER_API_SECRET = "srY2PdGOZJSsuQr7yDCFukhxAG3AMOf4e70p84UpJl3dedZ99k" 
ACCESS_TOKEN = "1091001075048566785-Rzbt4MQjzpdcGrG4fXKXsFMiY5bjgJ"
ACCESS_TOKEN_SECRET = "mPblWwMd4fCY1pqWO8WxaxrzMEnO6brduzJZJzABU1zHQ"

auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

tweets = api.home_timeline()

for tweet in tweets:
	print(twee.text)