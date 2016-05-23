#! /usr/bin/env python3
import functools

n = 13
with open('numbers_file') as f:
    numbers = f.read()

numbers =[int(number) for number in numbers.strip()]

highest = 0
for i in range(len(numbers) - (n - 1)):
    subset = numbers[i:i+n]
    product = functools.reduce(lambda x,y: x*y, subset)
    if product > highest:
        highest = product

print(highest)

    
