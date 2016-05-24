#! /usr/bin/env python3

# using datetime is kind of cheating, but I want to get more familiar with the
# module anyways...

import datetime

startdate = datetime.date(1901,1,1)
first_sunday =  startdate + datetime.timedelta(days = 6 - startdate.weekday())
enddate = datetime.date(2000,12,31)

date = first_sunday
count = 0
while date <= enddate:
	assert date.weekday() == 6
	if date.day == 1:
		count += 1
	date += datetime.timedelta(days=7)

print(count)
