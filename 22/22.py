#! /usr/bin/env python3
import csv
import string

with open('names.txt') as f:
	reader = csv.reader(f)
	names = [name for row in reader for name in row]

vals = {}
for index,letter in enumerate(string.ascii_uppercase):
	vals[letter] = index + 1

def letterscore(name):
	return sum(vals[letter] for letter in name)
	

score = 0
for index,name in enumerate(sorted(names)):
	score += (index + 1) * letterscore(name)

print(score)
