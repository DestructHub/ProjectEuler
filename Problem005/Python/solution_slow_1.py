#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
"""

# my ugly solution D: #brute-force:
divisors = [x for x in range(1, 21)]
x = 1
while True:
    smallest = True
    for i in divisors:
        if x % i != 0:
            smallest = False
            break
    if smallest:
        print(x)
        break
    x += 1
