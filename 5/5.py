#! /usr/bin/env python3
import functools
import sys

def numbers():
    x = 0
    while True:
        x += 1
        yield x

for number in numbers():
    for divisor in range(1,21):
        if number % divisor != 0:
            break
    else:
        print("Result found!")
        print(number)
        sys.exit(0)
