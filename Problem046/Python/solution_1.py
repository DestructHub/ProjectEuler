#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#


def sieve5(n):  # from primes algorithms on problem10
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p * p::2 * p] = [False] * ((n - p * p - 1) // (2 * p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result


def goldbach(odd, p):
    """check if some odd composite can be equal with p prime
    whose follow the equation: odd_composite == prime + 2 * x²
    """
    # that part is a analytical solution for get the x num:
    # the possible numbers to odd composite (not prime odd) is:
    # :: odd = prime  + 2 * x²
    # so, x = sqrt((odd - prime) / 2), whose prime + 2 < odd.

    # simplification can be done yet, but I will keep that way
    return odd == (p + 2 * int(((odd - p) / 2) ** 0.5) ** 2)


def solution(heuristic_start=10000):
    # i don't know the limit, so we start until 10.000 primes and composites
    primes = sieve5(heuristic_start)
    # n > 1 & doesn't primes
    composites = set(range(2, heuristic_start)) - set(primes)
    for odd in filter(lambda x: x % 2 != 0, composites):
        filtered_primes = filter(lambda x: odd > x - 2, primes)
        if not any(goldbach(odd, p) for p in filtered_primes):
            return odd

    return solution(heuristic_start*2)  # if don't find, try other ranges

if __name__ == '__main__':
    print(solution())
