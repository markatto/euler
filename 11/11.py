#! /usr/bin/env python3
import operator
import functools
import itertools

with open('grid') as f:
    data = f.read()

data = data.splitlines()
data = [[int(i) for i in line.split(' ')] for line in data]

dimension = len(data)
greatest_sum  = 0
greatest_adjacent = None

def adjacents():
    # diagonal down and right
    for y,x in itertools.product(range(dimension - 3), repeat=2):
        diagonal = []
        for i in range(4):
            diagonal.append(data[y+i][x+i])
        yield diagonal
    # diagonal up and right
    for y,x in itertools.product(range(3, dimension), range(dimension - 3)):
        diagonal = []
        for i in range(4):
            diagonal.append(data[y-i][x+i])
        yield diagonal
    # horizontal
    for y,x in itertools.product(range(dimension), range(dimension - 3)):
        horizontal = []
        for i in range(4):
            horizontal.append(data[y][x+i])
        yield horizontal
    # vertical
    for y,x in itertools.product(range(dimension - 3), range(dimension)):
        vertical = []
        for i in range(4):
            vertical.append(data[y+i][x])
        yield vertical
    

for adjacent in adjacents():
    current_sum = sum(adjacent)
    if current_sum > greatest_sum:
        greatest_sum = current_sum
        greatest_adjacent = adjacent

print(greatest_adjacent)
print("sum: {}".format(greatest_sum))
print("product: {}".format(functools.reduce(operator.mul, greatest_adjacent)))

