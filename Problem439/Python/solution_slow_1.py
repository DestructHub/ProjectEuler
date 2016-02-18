#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

# THAT IS A BOMB!

"""
Let d(k) be the sum of all divisors of k.
We define the function S(N) = ∑1≤i≤N ∑1≤j≤N d(i·j).
For example, S(3) = d(1) + d(2) + d(3) + d(2) + d(4) + d(6) + d(3) + d(6) + d(9) = 59.

You are given that S(10^3) = 563576517282 and S(10^5) mod 10^9 = 215766508.
Find S(10^11) mod 10^9 
"""

from functools import reduce


def gd(k):
    for x in range(1, k + 1):
        if k % x == 0:
            yield x


def d(k):
    return reduce(lambda x, y: x + y, gd(k))


def g(n):
    for x in range(1, n + 1):
        for y in range(1, n + 1):
            yield x * y


def s(n):
    dic = {}
    _sum = 0
    for i in g(n):
        if i not in dic:
            dic[i] = d(i)
        _sum += dic[i]

    return _sum

print(s(10 ** 11) % 10 ** 9)
