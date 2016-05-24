#! /usr/bin/env python3
from __future__ import division
import sys

def memoize(f):
    '''simple memoization decorator'''
    class memdict(dict):
        def __missing__(self, key):
            self[key] = f(key)
            return self[key]
    d = memdict()
    return d.__getitem__

def collatz(n):
    '''given the previous term, returns the next term in a collatz sequence'''
    if n <= 1:
        return 1
    if n % 2 == 0:
        return n // 2
    else:
        return n*3 + 1

@memoize # on cpython, this decreases runtime from ~1m3s to ~3.5s, pypy ~5s to ~1.5s
def collatz_len(n):
    '''return the length of the collatz sequence starting with n'''
    if n == 1:
        return 1
    else:
        return collatz_len(collatz(n)) + 1

sys.setrecursionlimit(1500)
search_max = 1000000
print(max((
    (i, collatz_len(i)) for i in range(search_max + 1)),
    key=lambda x: x[1]))
