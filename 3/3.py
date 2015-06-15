#! /usr/bin/env python3
import math

def primes_below(x):
    '''compute all primes below x'''
    # sieve[n] will be true if n is prime
    sieve = [True] * (x + 1)
    sieve[0] = False
    sieve[1] = False
    for index in range(2, len(sieve)):
        # not a prime; all multiples already marked
        if not sieve[index]:
            continue

        # mark all multilples of index as prime
        for i in range(index,len(sieve),index):
            # don't mark the first multilple as prime
            if i == index:
                continue
            sieve[i] = False

    return [i[0] for i in enumerate(sieve) if i[1]]

def largest_prime_factor(x):
    '''compute the largest prime factor of x'''

    # must be <= sqrt(x)
    primes = primes_below(math.ceil(math.sqrt(x))) 

    for prime in reversed(primes):
        if x % prime == 0:
            return prime

if __name__ == "__main__":
    print(largest_prime_factor(600851475143))
