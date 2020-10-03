import tweepy
from tweepy import OAuthHandler
from tweepy import Stream
import time
from tweepy.streaming import StreamListener
import json
from nltk.tokenize import word_tokenize
import os

from mmap import mmap

def preprocess(s):
    print(word_tokenize(s))

json_file = "mytweets.json"

filew=open(json_file, 'r+')

lookup = '}'

with filew as myFile:
    global index
    index=[]
    for num, line in enumerate(myFile, 1):
        if lookup in line[0]:
            index.append(num)
            print('leak found at line:', num) 
     
def bucket(bucket2, i, bucketk2):
    print('patching leak at ', i[-1])
    try:
        with bucket2 as b:
            
            for num, line in enumerate(b, 1):
                #print(num)
            
                if num >= i[-1]:
                    #print('d')
                    
                    #print(num)
                    b.close()
  
                else:
                    #print('3')
                    pass
                    
    except ValueError as e:
        print('finishing')
        
        with bucketk2 as b2:
            
            FinalJson=open('final-spread.json','w+')
            FinalJson.write('[')
            for num, line in enumerate(b2, 1):
                if num >= index[-1]:
                    #data = b2.readlines()
                    
                    FinalJson.writelines(''+'\n')
                
                    #print(num)
                    #print(line)
                    b2.close
                    b2=open('mytweets.json','r+')
                else:
                    #FinalJson.writelines('\n')
                    FinalJson.writelines(line)
                    pass
            FinalJson.writelines('}]')

            b2.close
        return True
        
bucketk=open(json_file,'r+')
bucketk2=open(json_file,'r+')
bucket(bucketk, index, bucketk2)
    
f = json.load(open('final-spread.json'))

for line in f:
    if 'extended_tweet' in line:

        preprocess(line['extended_tweet']['full_text'])

    else:
	
        preprocess(line['text'])
