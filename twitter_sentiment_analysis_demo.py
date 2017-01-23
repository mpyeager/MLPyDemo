import tweepy
from textblob import TextBlob

consumer_key = "ybYvSQdCc4OFnsEX0WZZR3DHd"
consumer_secret = "UPw2NXtTZnoAPS07lKxjY1LI5VakLv1jEM1SnJG0C3ejy5UQnl"

access_token = "18505899-uKMOQixny6KHC5gdqsBZdhabgpT6seq043Ph1TlCe"
access_token_secret = "4PdowtvG50jZsbsOCWN8s4Z8MBoIMzcG7SeykPZmXalrx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('SEARCH_TERM')

for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print(analysis.sentiment)