#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
Number letter counts
Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import json
from os.path import dirname
from os.path import join

# to work with stats.py
with open(join(dirname(__file__), 'p17_dic.json'), 'r') as f:
    dic = json.load(f)


def parser(string):
    if len(string) == 3:
        a, b, c = dic[string[0]], dic[string[1]], dic[string[2]]
        return a + ' and ' + b + '-' + c
    elif len(string) == 2:
        a, b = dic[string[0]], dic[string[1]]
        if int(string[0]) >= 10 and sum([int(x) for x in string]) > 100:
            conective = ' and '
        else:
            conective = '-'
        return a + conective + b
    else:
        return dic[string[0]]


def decomp(string):
    end = []
    if int(string) % 100 in range(10, 20):
        end = [str(int(string) % 100)]
        string = str((int(string) // 100) * 100)

    # LOOOOOOOOOOL
    return [str((int(string[x]) * 10 ** (len(string) - (x  + 1)))) for x in range(len(string)) if int(string[x]) != 0] + end


def clear(num):
    return (''.join([c for c in num if c not in ' -']))


def solution():
    nums = (decomp(str(x)) for x in range(1, 1001))
    cordial = (parser(x) for x in nums)
    clean = (clear(x) for x in cordial)
    answer = sum(len(num) for num in clean)
    return answer

print(solution())