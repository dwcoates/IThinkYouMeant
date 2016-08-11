#!/usr/bin/env python

# Originally planned to use a bloomfilter to check for anagrams,
# however instead it preprocesses WordNet dictionary into an anagram
# list file. Any two given words are encoded identically iff they
# contain the same family of letters, i.e., one word is a permutation
# of another. This is achieved by assigning each letter in the english
# language with a unique prime, and relying on the theory of the
# unique prime factorization of any given integer. Word sets never
# require decoding, as codes for anagram sets are hashed for
# reference, so anagram set lookups are easy, thus factorizing large
# numbers is never a needed operation.  Encoding of anagrams is done
# once in the preprocessing

# Unfortunately, this program will require likely some level of
# semantic parsing.  Choice is either to preserve semantic structure
# of tweet, or to take set of anagrams corresponding to words and
# tweet, and constructing a new sentence, which would require likely a
# set of semantic templates (a family of parts of speech). In either
# case, words with multiple parts of speech will have to have their
# active part of speech determined from context.

import tweepy
import time
import sys
from pybloom import BloomFilter  # still need to grab this dependency

codesfile = open(codes.dat, 'r')
codes = [code['number'] for code in codesfile]

# found on twitter application page
CONSUMER_KEY = codes[0]
CONSUMER_SECRET = codes[1]
ACCESS_KEY = codes[2]
ACCESS_SECRET = codes[3]

# authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# unfortunately I can't yet find a database for other parts of speech
partsOfSpeech = ["noun", "verb", "adj", "adv"]

dictionary = []
for PoS in partsOfSpeech:
    filename = "index." + PoS  # this is how WordNet names their data files
    dictionary += generateBloomFilter(open(filename, 'r'))

    # placeholder
while True:
    # ...tweepy magic for returning tweets ad nauseum goes here...
    anagrams = findAnagrams("", word)


def generateBloomFilter(file):
    "Generates the bloom filter for entries in file."
    # this probably isnt enough, need to look the data formatting over more
    # thoroughly
    d = BloomFilter(1000, 0.001)
    for line in file:
        d.add(line.split(1)[0])


def searchDicts(word):
    "Returns the dictionaries to which word belongs"
    entry = {"Word": word, "PoS": []}
    for pos in partsofspeech:
        if(word in dictionary[PoS]):
            entry["PoS"] += pos
    return entry


def findAnagrams(head, tail):
    "Finds all anagrams in database for head+tail and builds dictionary for these words plus"
    "their corresponding parts of speech. Has O(n!) complexity (not including searchDict(word) calls)."
    anagrams = []
    if len(tail) <= 1:
        if(len(entry=searchDicts(head + tail)) != 0):  # throw away anagrams that aren't real words
            anagrams += entry
        return anagrams

    for letter in tail:
        anagrams += findAnagram(head + letter, tail.replace(letter, ""))
    return anagrams
