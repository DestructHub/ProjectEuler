#!/usr/bin/env python
# coding=utf-8

# remove unnecessary range in square of sum (solution inspired by Manoel Vilela)

from functools import reduce

from sys import version_info

if version_info >= (3, 0):
    xrange = range

print(reduce(lambda x, y: x + y, xrange(1, 101)) ** 2 - ((100*101)/2))
