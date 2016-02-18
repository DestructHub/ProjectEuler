#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
Names scores
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

from os.path import join, dirname
from string import ascii_uppercase as alf

f = open(join(dirname(__file__), 'p022_names.txt'), 'r').read()[:-1]
l = sorted([x[1:-1] for x in f.split(',')])
s = lambda x: sum(((alf.index(y) + 1) for y in x))
print(sum((s(l[x]) * (x + 1) for x in range(len(l)))))