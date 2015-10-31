#Cymbolism.com dictionary

words = {'cute': {'fuchsia': .5424, 'aqua': .0929, 'yellow': .0757, 'purple': .0383, 'gold': .0327, 'orange': .0317, 'lime': .0270, 'red': .0253, 'blue': .0231, 'black': .0162, 'teal': .0157, 'white': .0150, 'brown': .0123, 'gray': .0118, 'green': .0118, 'silver': .0086, 'navy': .0086, 'maroon': .0074, 'olive': .0037},
        'easy': {'lime': .1722, 'aqua': .1400, 'white': .1272, 'yellow': .1197, 'blue': .0668, 'green': .0604, 'fuchsia': .0502, 'gold': .0470, 'silver': .0371, 'orange': .0354, 'teal': .0314, 'red': .0220, 'black': .0210, 'navy': .0168, 'gray': .0158, 'purple': .0143, 'brown': .0089, 'maroon': .0084, 'olive': .0052},
        'fun': {'yellow': .2614, 'fuchsia': .1716, 'lime': .1238, 'red': .0904, 'orange': .0792, 'gold': .0534, 'aqua': .0532, 'blue': .0456, 'purple': .0256, 'green': .0212, 'black': .0170, 'gray': .0116, 'navy': .0092, 'brown': .0078, 'maroon': .0066, 'teal': .0066, 'silver': .0058, 'white': .0058, 'olive': .0042}}


#Get all your tweets -- insert your twitter OAUTH credentials here

import os
os.environ['TW_CONSUMER_KEY']=''
os.environ['TW_CONSUMER_SECRET']=''
os.environ['TW_ACCESS_TOKEN']=''
os.environ['TW_ACCESS_TOKEN_SECRET']=''

from twutil import collect
collect.reinit()
d = collect.tweets_for_user('ewarmz')

#Count occurances of words from Cymbolism in tweets. Only search for whole words.

import re

def findWholeWord(w):
    return re.compile(r'\b({0})\b'.format(w), flags=re.IGNORECASE).search

count = {}

for tweet in tweets:
    for word in words.keys():
        if findWholeWord(word)(tweet['text']):
            count[word] = count.get(word, 0) + 1
            
print(count)

# Create sparse matrix

import numpy as np
from numpy import array as npa
from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.preprocessing import scale

#row headers for X
headers = npa(list(words.keys()))
counts = npa(list(count.values()))

colors = npa(list(words['cute'].keys()))
colors.sort()
print(colors)
vec = DictVectorizer()
X = vec.fit_transform(words.values())

#Calculate your spirit color!

import operator

scores = counts*X
results = dict(zip(colors,scores))
print(results)

max(results.items(), key=operator.itemgetter(1))[0]


