#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from itertools import permutations, chain
from sympy.ntheory import Sieve


class PrimePermutations(int):

    """
        Class to verify if a prime can be had prime permutation itself:
        permutations primes:
    """

    # class global variable, i only do that one time
    _primes = list(Sieve().primerange(1000, 9999))

    def __init__(self, x, min_permutations=3):
        self.num = x
        self.min = min_permutations

    @property
    def permutations(self):
        return set(map(int, (''.join(x) for x in permutations(str(self)))))

    @property
    def primes(self):
        return sorted([p for p in self.permutations if p in self._primes])

    @property
    def is_candidate(self):
        return len(self.primes) >= self.min

    def _zip(self, content):
        return zip(content, content[1:])

    @property
    def had_some_sequence(self):
        return any(x == y for x, y in self._zip(self.diff))

    @property
    def sequence(self):
        return [(x, y) for x, y in self._zip(self.primes) if y - x == self.max]

    @property
    def max(self):
        return max(self.diff, key=self.diff.count)

    @property
    def diff(self):
        return [y - x for x, y in self._zip(self.primes)]

    @property
    def concat(self):
        return ''.join(map(str, sorted(set(chain(*self.sequence)))))  # lol

    @classmethod
    def solution(cls):
        to_check = cls._primes.copy()  # make copy to not fuck the _primes
        while any(to_check):  # if not all check
            p = cls(to_check.pop())  # instantiate last prime
            if p.is_candidate:  # had at least 3 permutable primes?
                if p.had_some_sequence:  # had some sequence between?
                    return p.concat  # is the answer, concat
                for x in p.primes:  # remove checked primes
                    if x in to_check:  # remove checked primes
                        to_check.remove(x)


if __name__ == '__main__':
    print(PrimePermutations.solution())
