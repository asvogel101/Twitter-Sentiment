# Twitter Sentiments

Project to analyze Twitter streams and search for keywords. Work in progress. You will need access to the TWEEPY API.

## Dependencies 
- [vincent](https://vincent.readthedocs.io/en/latest/#)
- [tweepy](https://github.com/tweepy/tweepy)
- [nltk](https://github.com/nltk/nltk)

You will also need to install some `nltk` packages (`stopwords` and `punkt` I think?) from within the python interpretor. 

## Useful Documentation
- [Tokenizing words with nltk](https://pythonspot.com/tokenizing-words-and-sentences-with-nltk/)
- [Using defaultdict](https://medium.com/swlh/python-collections-defaultdict-dictionary-with-default-values-and-automatic-keys-305540540d2a)

## TODO

- Fix json bucket error when attempting to stream from previous stream and then tokenize

- Add more analysis tools

## HELP

- You must have access to the tweepy API in order for the application to work. Save your consumer key as a plaintext file named "consumerkey.txt" within the directory. Save your consumer secret as a plaintext file named "consumersecret.txt". Save your access token as a plaintext file named "accesstoken.txt". Save your access secret as a plaintext file named "accesstoken.txt". Make sure all keys are located in the main directory. 

- Run tweetfetcher.py to stream tweets. Then tokenize the tweets into a 'final-spread.json ' with tokenizer.py. Common.py is the only statistical analysis tool as of now. It features a word co-occurrence matrix and frequency of terms. 

- If attempting to restream, it is recommended that you delete the my-tweets.json and final-spread.json files, or move them to a different directory. Currently working on a way to implement continuous streaming within the same json doc. 
