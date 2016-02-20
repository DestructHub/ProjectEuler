#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from itertools import count
from sympy.ntheory import factorint


def solution(q):
    c = 0
    for p in count(start=1, step=1):
        if len(factorint(p)) == q:
            c += 1
            if c == 1:
                last = p
        else:
            c = 0

        if c == q:
            return last


print(solution(4))
