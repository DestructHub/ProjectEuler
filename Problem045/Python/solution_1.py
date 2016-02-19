#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from math import floor
from itertools import count


# triangle
# -> t = n² + n: n² + n - t = 0

# pentagonal (I)
# -> p = (3n² - n) / 2: 3n² - n -2p = 0

# hexagonal (II)
# -> h = (2n² - n) / 1: 2n² -n  -h = 0

# for t = p = h, we have to found the root of equations (I)
# and (II), whose are positive and integer. The root points
# to the n when p, h, or t exists for integers.
# so we compute the triangle nums after the last (285)
# and considering p = t, and h = t.

def quadratic(a, b, c):
    return (-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a)


def solution():
    for x in count(start=286, step=1):
        t = (x * x + x) // 2
        p = quadratic(3, -1, -2 * t)
        h = quadratic(2, -1, -1 * t)

        if floor(p) == p and floor(h) == h:
            return t

if __name__ == '__main__':
    print(solution())
