#! /usr/bin/env python3
import itertools
import collections
import sys

# You really want to run this with pypy

def triangle_number_gen():
    '''generate triangle numbers (1+2+3+...)'''
    n = 0
    x = 0
    while True:
        n += 1
        x += n
        yield x

def sieve_below(x):
    # sieve[n] is the factor count of n
    sieve = collections.OrderedDict()
    triangle_numbers = list(itertools.islice(triangle_number_gen(),0,n))
    for number in triangle_numbers:
        sieve[number] = 0

    for index in range(1, triangle_numbers[-1]):
        # mark all multiples of index
        for i in range(index,triangle_numbers[-1],index):
            if i in sieve:
                sieve[i] += 1
    return sieve



if __name__ == "__main__":
    n = 4096
    while True:
        sieve = sieve_below(n)
        for number in sieve:
            if sieve[number] > 500:
                print("{}: {}".format(number, sieve[number]))
                sys.exit(0)
        n = n * 2
        print("expanding to size {}".format(n))

