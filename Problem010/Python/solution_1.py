#!/usr/bin/env python2
# coding=utf-8
"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from primes import primes_list
from functools import reduce

print(reduce(lambda x, y: x + y, primes_list(2000000)))
