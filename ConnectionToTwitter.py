'''
Written by Aanchal Gupta and Ankeet Tendulkar
'''

import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener
import json

consumer_key = 'XXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
access_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

class MyListener(StreamListener):
    def on_data(self, data):
        json_load = json.loads(data)
        texts = json_load['text']
        coded = texts.encode('utf-8')
        s = str(coded)
        tweet = s[2:-1]

        if 'RT' not in tweet:
            print(tweet)
            textFile = open('result.txt', 'a', encoding='utf-8')
            textFile.write(tweet + "\n")
            textFile.close()
            #print(str(texts))
            return True

    def on_error(self, status):
        print(status)
        return True

twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#DonaldTrump'])
#twitter_stream.filter(track=['#HillaryClinton'])
