#!/usr/bin/env python
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from functools import wraps


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


class TruncatePrime(int):

    """
        Class to verify  if a prime is a truncate:
        Truncate prime example:  3797
        pop left: 3797 -> 379 -> 37 -> 3
        pop right: 3797 -> 797 -> 97 -> 7
    """

    def __init__(self, x):
        self.num = x
        self.string = str(x)
        self.len = len(self.string)

    def __add__(self, other):
        return self.num + other

    @property
    def left(self):
        return all([self.is_prime(x) for x in self.walk('left')])

    @property
    def right(self):
        return all([self.is_prime(x) for x in self.walk('right')])

    @property
    def self(self):
        return self.is_prime(self.num)

    def walk(self, orientation):
        if orientation is 'right':
            return (int(self.string[:x]) for x in range(1, self.len))
        elif orientation is 'left':
            return (int(self.string[x:]) for x in range(1, self.len))

    @memo
    def is_prime(self, x):
        if x < 2:
            return False
        for d in range(2, int(x ** 0.5) + 1):
            if x % d == 0:
                return False
        return True

    @property
    def is_truncate(self):
        if len(self.string) < 2:
            return False

        return self.self and self.left and self.right


def search_truncate(until=11):
    n = 0
    truncate_primes = []
    while len(truncate_primes) < until:
        t = TruncatePrime(n)
        if t.is_truncate:
            print('Found: {}'.format(t))
            truncate_primes.append(t)
        n += 1
    print('N-found: {}'.format(len(truncate_primes)))
    return sum(truncate_primes)

if __name__ == '__main__':
   print('Answer: {}'.format(search_truncate()))

