
import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import time
import datetime

from itertools import count

from tweepy.streaming import StreamListener
import json
from nltk.tokenize import word_tokenize
import os
consumer_key='WkotXcVWzijO9IVTqtGkHIVER'
consumer_secret='a0vCMOxXJnDWpIGpvUDsXS39abKM0SmEJQXLCHj8lrlxLUVldy'
access_token='1113322765640118272-uZJ9BorzzfVKAo5MgJhTnFVYlsOOVd'
access_secret='cHh1FhO1HELkOzCOYu6Q8hPrb4pvFviKlCSutobkGp9IG'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api=tweepy.API(auth)

f=open('mytweets.json','a',encoding='utf-8')
hashtag=str(input('Which hashtag? '))

class MyListener(StreamListener):
    _ids = count(1)

    def on_status(self, status):
        count = MyListener._ids
       
        if hasattr(status, "retweeted_status"):
            
            print("Passing on a RT")
            pass
             
                
        
        else:
            
            json.dump(status._json, f, ensure_ascii=False, indent=4)
            f.write(','+'\n')
            count = next(count)
            print('['+str(count)+'] ', "Success! Writing one entry.")

            
            return count
            
    def on_error(self, status):
        if status == 420:
            print("Twitter is limiting this account.")
            print(datetime.datetime.now())
            time.sleep(60*15)
        else:
            print("Error Status "+ str(status))


twitter_stream=Stream(auth, MyListener())
twitter_stream.filter(track=[hashtag], languages=["en"])





        

    
