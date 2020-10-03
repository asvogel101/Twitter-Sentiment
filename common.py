
###This Is testing GitHub ####


import json
from nltk.tokenize import word_tokenize
import os
import operator
from collections import Counter
import re
from nltk import bigrams
from mmap import mmap
from collections import defaultdict

def preprocess(s, lowercase=True):
    tokens = word_tokenize(s)
    if lowercase:
        tokens = [token.lower() for token in tokens]
    return tokens
 
com = defaultdict(lambda : defaultdict(int))
#need to add filtration system
from nltk.corpus import stopwords
import string

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via']
#terms_stop = [term for term in preprocess(tweet['text']) if term not in stop]

from nltk.tokenize import word_tokenize
search_word = None
tag = set()
if input('Any word you want to search co-occurence? y/n ') == 'y':
    search_word = input('Which word would you like to search for? ') 

count_search = Counter()

index = int(input("Set index of similarity deletion (Is negatively exponentional, set lower for less spam but lower sample size, higher for more spam but larger sample): "))
f = json.load(open('final-spread.json'))
count_all = Counter()
coutn = []
for line in f:
    
    texty = line['text']
    
    if texty[:index] in tag:
        #print(texty)
        pass
    
    elif 'extended_tweet' in line:
        coutn.append(1)
        #terms_all = [term for term in preprocess(line['extended_tweet']['full_text'])]
        terms_stoplong = [term for term in preprocess(line['extended_tweet']['full_text']) if term not in stop and not term.startswith(('@', '#','https','btc','bitcoin'))]
        if search_word in terms_stoplong:
            count_search.update(terms_stoplong)
        terms_bigrams = bigrams(terms_stoplong)
        count_all.update(terms_stoplong)
        #print(terms_stoplong)
        for i in range(len(terms_stoplong)-1):
            for j in range(i+1,len(terms_stoplong)):  
                w1, w2 = sorted([terms_stoplong[i],terms_stoplong[j]])
                if w1 != w2:
                    com[w1][w2] += 1
    else:
        coutn.append(1)
        #preprocess(line['text'])
        terms_stopshort = [term for term in preprocess(line['text']) if term not in stop and not term.startswith(('@','#','https','btc','bitcoin'))]
        if search_word in terms_stopshort:
            count_search.update(terms_stopshort)
        terms_all = [term for term in preprocess(line['text'])]
        terms_bigrams = bigrams(terms_stopshort)

        count_all.update(terms_stopshort)
        #print(terms_stopshort)
        for i in range(len(terms_stoplong)-1):
            for j in range(i+1,len(terms_stoplong)):  
                w1, w2 = sorted([terms_stoplong[i],terms_stoplong[j]])
                if w1 != w2:
                    com[w1][w2] += 1
    
    tag.add(texty[:index])

print('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||')   
print(count_all.most_common(50))
print('Sample size ', sum(coutn))
print('----------------------------------------------------------------------------------------------------------------------------------------------')
com_max = []
# For each term, look for the most common co-occurrent terms
for t1 in com:
    t1_max_terms = sorted(com[t1].items(), key=operator.itemgetter(1), reverse=True)[:5]
    for t2, t2_count in t1_max_terms:
        com_max.append(((t1, t2), t2_count))
# Get the most frequent co-occurrences
terms_max = sorted(com_max, key=operator.itemgetter(1), reverse=True)
print(terms_max[:30])
print('---------------------------------------------------------------------------------------------------------------------------------------------')
print(count_search.most_common(50))

import vincent
 
word_freq = count_search.most_common(20)
labels, freq = zip(*word_freq)
data = {'data': freq, 'x': labels}
bar = vincent.Bar(data, iter_idx='x')
bar.to_json('term_freq.json')
