#! /usr/bin/env python3

# What is the sum of the digits of the number 2**1000?
# again, python feels like cheating here...

print(sum((int(i) for i in str(2**1000))))
