# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 11:56:56 2017

@author: aldos
"""

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

from NLTKvid19_pickledmodule import sentiment


#consumer key, consumer secret, access token, access secret.
ckey="ucCZEgzcksTTBq2PaMtHg5UAW"
csecret="B8u2hx9Wap2Qki722kU53QgTOGI1LO2b0V0oD8eXkmAJoRk2rF"
atoken="75218878-eAMzFoBXODAwZLerUOfIUxLa2rTfmBYRJap8zrTAX"
asecret="1ly5CYOI8DCrIX76gFmg6sNsbOeAfIq43VMxlCeO0Vmoo"

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        
        tweet = all_data["text"]
        sentiment_value, confidence = sentiment(tweet)
        print(tweet, sentiment_value, confidence)
        
        if confidence >= 80:
            output = open("twitter_out.txt", "a")
            
            output.write(sentiment_value)
            output.write('\n')
            output.close()
        
        return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
output = open("twitter_out.txt", "r+")
output.truncate(0)
output.close()

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["fruit"])