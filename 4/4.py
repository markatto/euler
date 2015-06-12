#! /usr/bin/env python3
import itertools

palindromes = []
for x,y in itertools.combinations_with_replacement(range(100,1000),2):
    product = x * y
    if str(product) == ''.join(reversed(str(product))):
        palindromes.append(product)

print(max(palindromes))
