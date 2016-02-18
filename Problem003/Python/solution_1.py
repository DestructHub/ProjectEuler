#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from sys import version_info

if version_info >= (3, 0):
    xrange = range

"""
Largest prime factor
Problem 3
Published on Friday, 2nd November 2001, 06:00 pm; Solved by 264184

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def prime_gen(n):
    for i in xrange(2, n):
        prime = True
        if i % 2 == 0 and i != 2:
            continue
        sqrtp = int(i ** 1 / 2)
        for j in xrange(2, sqrtp):
            if j % 2 == 0:
                continue
            if i % j == 0:
                prime = False
                break
        if prime:
            yield i

num = 600851475143

for i in prime_gen(num):
    if num % i == 0:
        num /= i
    if num <= 1:
        print(i)
        break
