#! /usr/bin/env python3

def fib():
    '''generator for the fibonacci sequence'''
    yield 1
    yield 2

    x = 1
    y = 2
    while True:
        tmp = x + y
        x = y
        y = tmp
        yield y


total = 0
for x in fib():
    if x > 4000000:
        break
    if x % 2 == 0:
        total += x

print(total)
