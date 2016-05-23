#! /usr/bin/env python3

# We need to print the first 10 digits of the sum of a bunch of huge numbers.
# Doing this in python is basically cheating because we get bigint support for free.
# This would be pretty easy to do without bigints, however, because you only need 10 digits of precision; using a floating-point datatype will be accurate enough.
numbers = []
with open('numbers.txt', 'r') as f:
    for line in f:
        numbers.append(int(line.strip()))

print(str(sum(numbers)))
