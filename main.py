#!/usr/bin/env python

##################################################################################
##  Dodge Coates                                                                ##
##                                                                              ##
##  A Twitter bot that accepts tweets and scrambles their words into anagrams,  ##
##  then those anagrams around into a new, coherent sentence. For now, the new  ##
##  sentence will have the same structure. This may be extended later.          ##
##                                                                              ##
##################################################################################

# There should be a anagrams database, and not just a dictionary. Will need to write a script
# to WordNet database into anagrams list

import tweepy, time, sys
from pybloom import BloomFilter # still need to grab this dependency

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
    filename = "index." + PoS # this is how WordNet names their data files
    dictionary += generateBloomFilter(open(filename, 'r'))

    # placeholder
while True:
    # ...tweepy magic for returning tweets ad nauseum goes here...
    anagrams = findAnagrams("", word)


def generateBloomFilter(file):
    "Generates the bloom filter for entries in file."
    # this probably isnt enough, need to look the data formatting over more thoroughly
    d = BloomFilter(1000, 0.001)
    for line in file:
        d.add(line.split(1)[0])

def searchDicts(word):
    "Returns the dictionaries to which word belongs"
    entry =  {"Word": word, "PoS": []}
    for pos in partsofspeech:
        if(word in dictionary[PoS]):
            entry["PoS"] += pos
    return entry

def findAnagrams(head, tail):
    "Finds all anagrams in database for head+tail and builds dictionary for these words plus"
    "their corresponding parts of speech. Has O(n!) complexity (not including searchDict(word) calls)."
    anagrams = []
    if len(tail) <= 1:
        if(len(entry = searchDicts(head+tail)) != 0): # throw away anagrams that aren't real words
            anagrams += entry
        return anagrams

    for letter in tail:
        anagrams += findAnagram(head+letter, tail.replace(letter, ""))
    return anagrams;
