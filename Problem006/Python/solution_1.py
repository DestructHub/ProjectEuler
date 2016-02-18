#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from functools import reduce

from sys import version_info

if version_info >= (3, 0):
    xrange = range

"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
12 + 22 + ... + 102 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 552 = 3025

Hence the difference between the sum of the squares
of the first ten natural numbers and the square of the
sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of
the first one hundred natural numbers and the square of the sum

"""

print(reduce(lambda x, y: x + y, xrange(1, 101)) ** 2 - reduce(lambda x, y: x + y ** 2, xrange(1, 101)))
