#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from functools import reduce
import sys

if sys.version_info > (3, 0):
    xrange = range
    long = int

"""
Factorial digit sum
Problem 20

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

print(reduce(long.__add__, map(long, str(reduce(long.__mul__, map(long, xrange(1, 100)))))))
