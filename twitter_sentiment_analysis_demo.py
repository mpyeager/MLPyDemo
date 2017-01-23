import tweepy
from textblob import TextBlob

#Ensure that you have a Twitter account linked to a mobile phone number, then
#generate your keys and secrets below from the Application Management section of
#the Twitter developer portal.

consumer_key = "INSERT_YOUR_CONSUMER_KEY"
consumer_secret = "INSERT_YOUR_CONSUMER_KEY_SECRET"

access_token = "INSERT_YOUR_ACCESS_TOKEN"
access_token_secret = "INSERT_YOUR_ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('SEARCH_TERM')

for tweet in public_tweets:
		print(tweet.text)
		analysis = TextBlob(tweet.text)
		print(analysis.sentiment)
