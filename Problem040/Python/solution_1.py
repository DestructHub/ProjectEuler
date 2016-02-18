#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from functools import reduce
from itertools import count


def frac_series_generator():
    '''each n after 0.1 from 0.12345678910111213...'''
    for w in count(start=1, step=1):
        for s in str(w):
            yield s


def search_digit_by_index(indexes):
    '''get the digits of indexes of frac_series'''
    limit = max(indexes)
    digits = {x: 0 for x in indexes}
    for c, n in enumerate(frac_series_generator()):
        if c + 1 in digits:
            digits[c + 1] = int(n)
        if c + 1 >= limit:
            break
    return digits.values()


def main():
    indexes = [1, 10, 100, 1000, 10000, 100000, 1000000]
    print(reduce(int.__mul__, search_digit_by_index(indexes)))

if __name__ == '__main__':
    main()
