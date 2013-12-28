#! /usr/bin/python

x=1
while True:
	nums = [set(str(i*x)) for i in range(1,7)]
	if nums[1:] == nums[:-1]:
		print(nums)
		print(x)
		break
	x += 1

