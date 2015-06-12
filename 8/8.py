#! /usr/bin/env python3
import functools

with open('numbers_file') as f:
    numbers = f.read()

numbers =[int(number) for number in numbers.strip()]

highest = 0
for i in range(len(numbers) - 12):
    subset = numbers[i:i+13]
    product = functools.reduce(lambda x,y: x*y, subset)
    if product > highest:
        highest = product

print(highest)

    
