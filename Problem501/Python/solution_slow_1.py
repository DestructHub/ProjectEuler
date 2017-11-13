#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

# PROBABLY THAT IS REALLY WRONG

"""
Eight Divisors
Problem 501

The eight divisors of 24 are 1, 2, 3, 4, 6, 8, 12 and 24.
The ten numbers not exceeding 100 having exactly eight divisors are 24, 30, 40, 42, 54, 56, 66, 70, 78 and 88.
Let f(n) be the count of numbers not exceeding n with exactly eight divisors.
You are given f(100) = 10, f(1000) = 180 and f(10^6) = 224427.
Find f(10^12).
"""

def d(n):
    return set(reduce(list.__add__,  [[i, n//i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0]))

def f(n):
    return sum([1 for x in xrange(2, n) if len(d(x)) == 8])

def f_p(n):
    last = 0
    for x in xrange(2, n):
        if len(d(x)) == 8:
            print x, (x - last)
            last = x
    return last

# Another comment

f_p(10 ** 12)
