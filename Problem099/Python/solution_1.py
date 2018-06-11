#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#


"""
Largest exponential
Problem 99

Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806
would be much more difficult, as both numbers
contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'),
a 22K text file containing one thousand lines with a base/exponent
pair on each line,
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the
numbers in the example given above.
"""
from math import log
from os.path import dirname, join

filedic = join('../p099_base_exp.txt')

dic_evalued = {}
with open(filedic, 'r') as f:
    nums = f.readlines()
    for line in range(len(nums)):
        num = nums[line].strip()
        base, exp = num.split(',')
        value = log(int(base)) * int(exp)
        dic_evalued[value] = line + 1

print(dic_evalued[max(dic_evalued)])
