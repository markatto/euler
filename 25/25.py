#! /usr/bin/env python3
import sys

# naive recursion
def fib(n):
	if n <= 2:
		return 1
	else:
		return (fib(n-1) + fib(n -2))

def memodict(f):
	class memodict(dict):
		def __missing__(self, key):
			ret = self[key] = f(key)
			return ret 
	return memodict().__getitem__

# memoized recursion
def memoize(f):
	class cachedict(dict):
		def __missing__(self, key):
			x = self[key] = f(key)
			return x 
	return cachedict().__getitem__

@memoize
def mfib(n):
	if n <= 2:
		return 1
	else:
		return (mfib(n-1) + mfib(n -2))

#generator using a loop
def ifib():
	x = 1
	y = 1
	yield 1
	yield 1
	while True:
		ret = x + y
		yield ret
		y = x
		x = ret

i = 1
g = ifib()
while True:
	x = g.__next__()
	if x > 10**999:
		print('%s: %s'% (i, x))
		sys.exit(0)
	i +=1
	
	
