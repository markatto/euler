#! /usr/bin/env python3
import itertools
import string
import re
import sys

with open('cipher1.txt') as f:
    data = f.read()

# data in file is actually numbers
data = [int(i) for i in data.strip().split(',')]

# get a wordlist that's randomly on disk
with open('/usr/share/dict/words') as f:
    wordlist = f.read().strip().split('\n')

# all possible 3-character keys
keys = itertools.permutations([ord(i) for i in string.ascii_lowercase], 3)

# xor the data with the key
def decode(data, key):
    # repetitively return the key
    def key_extend(key):
        while True:
            for i in key:
                yield i

    decoded_data = [i[0] ^ i[1] for i in zip(data, key_extend(key))]
    return decoded_data
    
    

for key in keys:
    decoded_string = ''.join([chr(i) for i in decode(data, key)])
    lowercase_string = decoded_string.lower()

    
    words = lowercase_string.split()

    words_in_dict = 0
    for word in words:
        if word in wordlist:
            words_in_dict += 1

    # simple heuristic; if over half the words are in our dictionary
    if words_in_dict / len(words) > 0.5:
        print(decoded_string)
        print("character sum: {}".format(sum([ord(c) for c in decoded_string])))

