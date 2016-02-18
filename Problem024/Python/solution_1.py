#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""

Lexicographic permutations
Problem 24

A permutation is an ordered arrangement of objects.
For example, 3124 is one possible permutation of the
digits 1, 2, 3 and 4. If all of the permutations are
listed numerically or alphabetically, we call it lexicographic order.
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the
digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""


def factorial(n):
    return 1 if n < 1 else n * factorial(n - 1)


# let the entry of element number of the sorted element
def problem24(element):
    from string import digits
    answer = ''
    nums = list(digits)
    while len(nums) != 0:
        # calculate the periodic of the unitary decimal actual
        factor_num = factorial(len(nums) - 1)
        # verify which must be the number of digit actual
        order = element//factor_num
        if element % factor_num != 0:
            order = element//factor_num + 1
        # keep only the rest of periodicity, whose we say which number is.
        order %= len(nums)
        # insert the value on final of string
        answer += nums.pop(order - 1)

    return answer

print(problem24(10 ** 6))
