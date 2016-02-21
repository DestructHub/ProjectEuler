#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from functools import wraps
from itertools import combinations as comb

LIMIT = 1000


def memo(fn):
    """Memorization decorator"""

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


def quadratic(a, b):
    """quadratic function abstraction"""
    def func(n):
        return n * n + a * n + b
    return func


@memo
def isprime(n):
    """memorized prime evaluation, 2x more faster on that algorithm"""
    for p in range(2, int(abs(n) ** 0.5) + 1):
        if n % p == 0:
            return False

    return True


def eval_func(func):
    """eval func which primes will generate"""
    n = 0
    while True:
        prime = isprime(func(n))
        if prime:
            n += 1
        else:
            return n


def search(limit):
    """search for the best a, b coefficients for a quadratic func prime gen"""
    coffs = {}
    for t in comb(range(-limit, limit + 1), 2):
        coffs[t] = max([eval_func(quadratic(a, b)) for a, b in [t, t[::-1]]])

    return max(coffs, key=lambda x: coffs[x])


def main():
    from functools import reduce
    print(reduce(int.__mul__, search(LIMIT)))

if __name__ == '__main__':
    main()
