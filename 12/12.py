#! /usr/bin/env python3
import itertools
import collections
import sys

# generate triangle numbers (1+2+3+...)
def triangle_number_gen():
    n = 0
    x = 0
    while True:
        n += 1
        x += n
        yield x

def count_divisors(x):
    '''this is waay too slow, but it reminds me of haskell so I'm leaving it here'''
    return sum((1 for i in range(1, x + 1) if x % i == 0))

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
    n = 32
    while True:
        sieve = sieve_below(n)
        for number in sieve:
            print("{}: {}".format(number, sieve[number]))
            if sieve[number] > 500:
                print(number)
                sys.exit(0)
        n = n * 2

