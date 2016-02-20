#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from functools import wraps
from os.path import dirname, join


def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result
    return wrapper


def load_words():
    with open(join(dirname(__file__), "p042_words.txt")) as f:
        words = f.read().strip("\n").split(",")
    return [x.lower().strip("\"") for x in words]


def string_to_num(string):
    from string import ascii_lowercase as alpha
    return sum([alpha.index(x) + 1 for x in string])


def triangles():
    from itertools import count
    for n in count(start=1, step=1):
        yield ((n + 1) * n) // 2


@memo
def is_triangle(num):
    for t in triangles():
        if num == t:
            return True
        if t > num:
            return False


def solution():
    return sum(1 for x in load_words() if is_triangle(string_to_num(x)))


if __name__ == '__main__':
    print(solution())
