
# Twitter Retweet Bot using Python

A Python built twitter retweet bot using Tweepy. Searches and retweets based on hashtag or keyword. Can do for multiple keywords, or hashtags. It can be used for automation and marketing purposes.

## What You Need 

-   [Tweepy](http://www.tweepy.org/)  - An easy-to-use Python library for accessing the Twitter API.

    `pip install tweepy`
-	Make a [Twitter Developer Account](https://developer.twitter.com/en).
-   Make sure you fully understand  [Twitter's Rules on Automation](https://support.twitter.com/articles/76915). Play nice. Don't spam!
- And you need to have [Heroku Account](https://dashboard.heroku.com/).

## Instructions

-   Create a new directory to contain all of your retweet bot files.

	`mkdir retweet-bot`
- Follow all the steps as shown in this [YouTube Video](https://youtu.be/lJdH9WWkd24)

-   Create a new  [Twitter Application](https://apps.twitter.com/app/new). This is where you'll generate your keys, tokens, and secrets.
-   Fill in your keys, tokens, and secrets in the credentials.py file.
-   Check comments in bot.py to tweak the retweet bot to your liking.
-   The example demonstrates a single hashtag value, but you can tweak the code to search multiple hashtags. Example:

	`q= #nifty50 OR #sensex`

-   Run your bot.py script.

	`python bot.py`
-	If it runs without any errors now it need to be deploy in [Heroku](https://dashboard.heroku.com/).
-	Once deployment done you're good to go you have successfully created a twitter bot. Enjoy!!

## For Heroku
You need to make three other files:
- runtime.txt (Includs Python Version `python-3.8.1`)
- requirements.txt (`pip freeze > requirements.txt`)
- Procfile (`worker: python bot.py`)

## Additional Information

-   Note: Make sure that your bot.py and credentials.py files are, obviously, in the same directory.
- If you stuck any where you can contact me in my [Twitter](https://twitter.com/imanishbarnwal) or [LinkedIn](https://www.linkedin.com/in/imanishbarnwal/) I will be glad to help you.
- And you must checkout my another [twitter bot](https://twitter.com/mlb0t) which share information related to Machine Learning.
