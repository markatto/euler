#! /usr/bin/env python3
from itertools import combinations_with_replacement
from math import sqrt,floor
from functools import reduce
from operator import mul

n = 1000

def is_pythagorean_triplet(triplet):
	'''a**2 + b**2 == c**2'''
	t = sorted(triplet) # c needs to be the biggest one
	return triplet[0]**2 + triplet[1]**2 == triplet[2]**2

triplets = combinations_with_replacement(range(1, n), 3) 
triplets = (t for t in triplets if sum(t) == n and is_pythagorean_triplet(t))

print([reduce(mul, triplet) for triplet in triplets])

