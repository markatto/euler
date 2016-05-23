#! /usr/bin/env python3
import itertools
from operator import mul
from functools import reduce

with open('grid') as f:
    data = f.read()

data = data.splitlines()
data = [[int(i) for i in line.split(' ')] for line in data]

def adjacents(grid):
    dimension = len(grid)
    # diagonal down and right
    for y,x in itertools.product(range(dimension - 3), repeat=2):
        diagonal = []
        for i in range(4):
            diagonal.append(grid[y+i][x+i])
        yield diagonal
    # diagonal up and right
    for y,x in itertools.product(range(3, dimension), range(dimension - 3)):
        diagonal = []
        for i in range(4):
            diagonal.append(grid[y-i][x+i])
        yield diagonal
    # horizontal
    for y,x in itertools.product(range(dimension), range(dimension - 3)):
        horizontal = []
        for i in range(4):
            horizontal.append(grid[y][x+i])
        yield horizontal
    # vertical
    for y,x in itertools.product(range(dimension - 3), range(dimension)):
        vertical = []
        for i in range(4):
            vertical.append(grid[y+i][x])
        yield vertical
    
print(max((reduce(mul, a) for a in adjacents(data))))
