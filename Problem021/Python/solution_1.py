#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from functools import reduce

"""
Amicable numbers
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

# FUCK D: ? i WROTE THIS? MY LEVEL OF OBSCURITY IS MORE HIGHER WHOSE I THOUGH...
def d(n):
	return sum(sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))[:-1])

print(sum(x for x in range(1, 10000) if d(x) > 0 and x != d(x) and x == d(d(x))))