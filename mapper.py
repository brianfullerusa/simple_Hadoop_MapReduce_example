#!/usr/bin/env python
import sys
import string
from sklearn.feature_extraction import stop_words



# get all lines from stdin
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # make the text lower case
    line = line.lower()

    # remove punctuation
    #exclude = set(string.punctuation)
    #line = ''.join(ch for ch in line if ch not in exclude)

    # split the line into words; splits on any whitespace
    words = line.split()

    # set stopwords
    # stopwords = set(['the', 'and'])
    stopwords = set(stop_words.ENGLISH_STOP_WORDS)

    # output tuples (word, 1) in tab-delimited format
    for word in words:
        if word not in stopwords:
          print '%s\t%s' % (word, "1")
