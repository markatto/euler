#! /usr/bin/env python3
from itertools import combinations_with_replacement
from math import sqrt,floor
from functools import reduce
from operator import mul

triplets = [x for x in combinations_with_replacement(range(1000), 3) if sum(x) == 1000 and (x[0]**2 + x[1]**2 == x[2]**2 or x[0]**2 + x[2]**2 == x[1]**2 or x[1]**2 + x[2]**2 == x[0]**2)]

print([reduce(mul, triplet) for triplet in triplets])

