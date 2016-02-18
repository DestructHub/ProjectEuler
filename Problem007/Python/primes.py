#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from sys import version_info

if version_info > (3, 0):
    xrange = range


def primeGen(n):
    for i in xrange(2, n):
        prime = True
        if i % 2 == 0 and i != 2:
            continue
        sqrtp = int(i ** 1 / 2)
        for j in xrange(2, sqrtp):
            if j % 2 == 0:
                continue
            if i % j == 0:
                prime = False
                break
        if prime:
            yield i


def primeGenEff(n):
    pp = 2
    yield pp
    pp += 1
    tp = [pp]
    ss = [2]
    while pp < n:
        pp += ss[0]
        test = True
        sqrtpp = pp ** 1/2
        for a in tp:
            if a > sqrtpp:
                break
            if pp % a == 0:
                test = False
                break
        if test:
            tp.append(pp)
            yield pp


def sieve5(n):
    """Return a list of the primes below n."""
    prime = [True] * n
    result = [2]
    append = result.append
    sqrt_n = (int(n ** .5) + 1) | 1    # ensure it's odd
    for p in range(3, sqrt_n, 2):
        if prime[p]:
            append(p)
            prime[p*p::2*p] = [False] * ((n - p*p - 1) // (2*p) + 1)
    for p in range(sqrt_n, n, 2):
        if prime[p]:
            append(p)
    return result
