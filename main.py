import os
import sys
import time
import random
import tweepy
from dotenv import load_dotenv
import keys




auth = tweepy.OAuthHandler(keys.api_key, keys.api_secret)
auth.set_access_token(keys.access_token, keys.access_token_secret)  
api = tweepy.API(auth)


keywords = '#opensource AND #Python OR #DataScience'

#Maximum limit of tweets to be interacted with
maxNumberOfTweets = 500

#To keep track of tweets published
count = 0


for tweet in tweepy.Cursor(api.search_tweets, keywords).items(maxNumberOfTweets):
    try:
        print('Found tweet by @' + tweet.user.screen_name)

        #Publishing retweet
        tweet.retweet()

        #Updating count for each successfull retweet
        count = count + 1
        print('Retweet #' + str(count) + ' published successfully.')

        #Random wait time
        timeToWait = random.randint(95, 115)
        print("Waiting for "+ str(timeToWait) + " seconds")
        for remaining in range(timeToWait, -1, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rOnwards to next tweet!\n")

    except tweepy.errors.Forbidden:
        pass
    except tweepy.TweepError as e:
        print('Error: ' + e.args[0][0]['message'])
    except StopIteration:
        break