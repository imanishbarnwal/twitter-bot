import tweepy 
from time import sleep

# Import in your Twitter application keys, tokens, and secrets.
# Make sure your credentials.py file lives in the same directory as this .py file. 
from credentials import * 

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
auth.set_access_token(access_token, access_token_secret) 
api = tweepy.API(auth)

# Twitter bot setting for liking Tweets 
LIKE = True

# Twitter bot setting for following user who tweeted 
FOLLOW = False

print("Twitter bot which retweets, like tweets and follow users") 
print("Bot Settings") 
print("Like Tweets :", LIKE) 
print("Follow users :", FOLLOW) 

# Change the hashtags by your choice

for tweet in tweepy.Cursor(api.search, q = ('#nifty50 OR #sensex OR #stocks -filter:retweets'),lang='en').items(): 
	try: 
		print('\nTweet by: @' + tweet.user.screen_name) 

		tweet.retweet() 
		print('Retweeted the tweet') 

		# Favorite the tweet 
		if LIKE: 
			tweet.favorite() 
			print('Favorited the tweet') 

		# Follow the user who tweeted 
		# check that bot is not already following the user 
		if FOLLOW: 
			if not tweet.user.following: 
				tweet.user.follow() 
				print('Followed the user') 
		
		# Twitter bot sleep time settings in seconds. Use large delays so that you account will not banned
		sleep(300) # 300 seconds = 5 minutes

	except tweepy.TweepError as e: 
		print(e.reason) 

	except StopIteration: 
		break
