#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
Counting fractions
Problem 72

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?
"""

class Rational(object):

    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
        self.num = str(n) + '/' + str(d)

    def __str__(self):
        return self.num

    def __add__(self, add):
        if isinstance(add, int):
            self.numerator += self.denominator * add
        elif isinstance(add, float):
            pass
        elif isinstance(add, Rational):
            self.numerator = self.numerator*add.denominator + add.numerator*self.denominator
            self.denominator = add.denominator*self.denominator

        self.update()
        return self.num

    def update(self):
        if self.denominator == 1:
            num = str(self.numerator)
        else:
            num = str(self.numerator)  + '/' + str(self.denominator)
        self.num = num

    def reduce(self):
        nums = (self.numerator, self.denominator)
        a = max(nums)
        b = min(nums)
        while b != 0:  # menor divisor comum
            a, b = b, a % b
        self.numerator /= a
        self.denominator /= a
        self.update()


def solution():
    proper_fractions = []
    test = 10 ** 6
    r_d = range(2, test + 1)
    r_n = range(2, test)
    for d in r_d:
        for n in r_n:
            if n > d:
                break
            f = Rational(n, d)
            f.reduce()
            if f.denominator != 1:
                proper_fractions.append(f)
    return len(set(proper_fractions))

if __name__ == '__main__':
    print(solution())
