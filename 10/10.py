#! /usr/bin/env python3

# hacked in with a symlink because we're not really doing modules
# and relative imports suck
from problem_3 import primes_below

print(sum(primes_below(2000000)))
