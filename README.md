
# Twitter Retweet Bot using Python

A Python-built Twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword. Can do multiple keywords, or hashtags.

## What You Need 

-   [Tweepy](http://www.tweepy.org/)  - An easy-to-use Python library for accessing the Twitter API.

    `pip install tweepy`
-	Make a [Twitter Developer Account]([https://developer.twitter.com/en](https://developer.twitter.com/en)).
-   Make sure you fully understand  [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam!
- And you need to have [Heroku Account](heroku.com).

## Instructions

-   Create a new directory to contain all of your retweet bot files.

	`mkdir retweet-bot`
- Follow all the steps here 

-   Create a new  [Twitter Application](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
-   Fill in your keys, tokens, and secrets in the credentials.py file.
-   Check comments in bot.py to tweak the retweet bot to your liking.
-   The example demonstrates a single hashtag value, but you can tweak the code to search multiple hashtags. Example:

	`q= #nifty50 OR #sensex`

-   Run your bot.py script.

	`python bot.py`
-	If it runs without any errors now it need to be deploy in [Heroku](heroku.com).
-	Once deployment done you're good to go you have successfully created a twitter bot. Enjoy!!

## Additional Information

-   Note: Make sure that your bot.py and credentials.py files are, obviously, in the same directory.
- If you stuck any where you can contact me in my [Twitter]([https://twitter.com/imanishbarnwal](https://twitter.com/imanishbarnwal)) or [LinkedIn]([https://www.linkedin.com/in/imanishbarnwal/](https://www.linkedin.com/in/imanishbarnwal/)) I will be glad to help you.
- And you must checkout my another [twitter bot]([https://twitter.com/mlb0t](https://twitter.com/mlb0t)) which share information related to Machine Learning.
