#! /usr/bin/env python3
import itertools

pyramid = []
with open('data.txt', 'r') as f:
	for line in f:
		pyramid.append([int(i) for i in line.strip().split(' ')])

for line in pyramid:
	print(line)

size = len(pyramid)

# 0 = go left, 1 = go right
paths = itertools.product((0,1), repeat=size - 1)

def walk_path(path):
	# start at the top
	sum = 0
	current_column = 0
	sum = pyramid[0][0]
	
	for index ,move in enumerate(path, start=1):
		# 0 = we go left, 1 = we go right
		current_column += move
		sum += pyramid[index][current_column]

	return sum

print(max(walk_path(path) for path in paths))
