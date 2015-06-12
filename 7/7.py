#! /usr/bin/env python3

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

def powers_of_2():
    x = 1
    while True:
        x = x * 2
        yield x

for limit in powers_of_2():
    primes = primes_below(limit)
    if len(primes) < 10001:
        continue
    else:
        print(primes[10000])
        break

