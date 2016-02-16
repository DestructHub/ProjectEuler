#!/usr/bin/env python
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

"""

    THAT IS A WRONG APPROACH FOR THIS PROBLEM! SLOWWWWWW

"""


"""
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""


# black magic divisors
def divisors(n):
    from functools import reduce
    to_reduce = [[i, n // i]
                 for i in range(1, int(n ** 0.5) + 1) if n % i is 0]
    return set(reduce(list.__add__, to_reduce))


def hnum(n, d):
    return d + (n // d)


class prime_divisors(object):

    """
        The solution provider from the depth of hell
    """

    def __init__(self, max_value):
        self.max = max_value
        self.primes = [2]
        self.hell_numbers = []
        self.run_from_hell()

    @property
    def sum(self):
        return sum(self.hell_numbers)

    def is_hell(self, n):
        return all([0 for d in divisors(n) if hnum(n, d) not in self.primes])

    def next_prime(self):
        for p in range(3, self.max + 2):

            is_prime = True
            for prime in self.primes:
                if p % prime == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes += [p]
            else:
                continue

            # print('next_prime: {}'.format(p))
            yield p

    def run_from_hell(self):
        # it's only possible even numbers, because:
        # if n = 2k + 1
        # and d = n
        # 2k + 1 + [2k + 1]/[2k + 1]
        # 2k + 1 + 1 => 2k + 2
        # even + even = even
        # if even, unique primes is two
        # but two don't is a hell number: 2 + 1/2: 2.5
        for n in range(2, self.max + 1, 2):
            if n > self.primes[-1]:
                for p in self.next_prime():
                    if p > n:
                        break
            if self.is_hell(n):
                self.hell_numbers += [n]
                # print('matched: {}'.format(n))


def main():
    w = prime_divisors(100000000)
    print(w.sum)


if __name__ == '__main__':
    main()
