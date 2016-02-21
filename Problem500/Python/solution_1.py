#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

import heapq
from sympy.ntheory import Sieve, prime  # I tired... more prime algorithms....


def primes_list(n):
    """Return the list of [2,..., n] n-th primes"""
    return [x for x in Sieve().primerange(2, prime(n))]


def smallest_integer(k, modulus=None):
    """Calculate the smallest number with 2**k divisors.

    The math stuff about this in a simply way

    The achieve is got the all range of primes [p_0 ** x,  p_n ** z]
    multiplied with factors minimized, even the smallest.

    For example the 120 on factored prime form is:
        120 = 2³ * 3¹ * 5¹,
    by the formula we got the numbers divisors that way:
    (3 + 1) (1 + 1) (1 + 1) => 4 * 2 * 2 = 16 divisors!

    So the formula is:
        if p = (a ** x) * (b ** y) * (c ** z)...
        div(p) = (x + 1) * (y + 1) * (z + 1)...

    Anyway, because 2 ** k, so k = x + y + z.

    Since a_n < b_m and a_n, b_m are primes nums,
    for a smallest integer with d divisors
    we want (a_n ** x_i) < (b_m ** y_j)... and existence of
    primes [a_n, b_m] are maximized.
    That way, the p num will be minimized.

    Because that, we use a heap queue, to get ever
    the smallest num and push the used with the cost:

    pop: smallest from primes costed with use
    push: p ** 2

    That way if the num was selected again,
    he'll be costed with x ** 2.

    As we have an expected num of 2 ** k divisors, we need
    iterate the heap k times. For each k, is a operation with more
    one divisor prime or factor.

    So the algorithm is O(K), considering the prime calculation
    stuff apart. Runs about 3s (more slow part is prime getting)

    See an iteration for execution of smallest_integer(k=4):

    Initial Heap with 4-th: [2, 3, 5]
    Heap: [2, 3, 5]
    Pop: 2 | Push: 4 => n = 1 * 2
    Heap: [3, 5, 4]
    Pop: 3 | Push: 9 => n = 2 * 3
    Heap: [4, 5, 9]
    Pop: 4 | Push: 16 => n = 6 * 4
    Heap: [5, 9, 16]
    Pop: 5 | Push: 25 => n = 24 * 5
    Answer: 120

    n = 2 * 3 * 4 * 5 = 120! = 2³ * 3 * 5

    Other example smallest_integer(k=6):

    Initial Heap with 6-th: [2, 3, 5, 7, 11]
    Heap: [2, 3, 5, 7, 11]
    Pop: 2 | Push: 4 => n = 1 * 2
    Heap: [3, 4, 5, 11, 7]
    Pop: 3 | Push: 9 => n = 2 * 3
    Heap: [4, 7, 5, 11, 9]
    Pop: 4 | Push: 16 => n = 6 * 4
    Heap: [5, 7, 9, 11, 16]
    Pop: 5 | Push: 25 => n = 24 * 5
    Heap: [7, 11, 9, 16, 25]
    Pop: 7 | Push: 49 => n = 120 * 7
    Heap: [9, 11, 25, 16, 49]
    Pop: 9 | Push: 81 => n = 840 * 9
    Answer: 7560

    n = 2 * 3 * 4 * 5 * 7 * 9 = 2³ * 3 ³ * 5 * 7

    So well:
       (3 + 1) (3 + 1) (1 + 1) (1 + 1) = 4 * 4 * 2 * 2
       => 4² * 2² = 2 ** 6

    CQD.

    """
    n = 1  # our last value

    # condition, that working only for k > 1
    costs = primes_list(k)  # more than necessary
    # print("Initial Heap with {}-th: {}".format(k, costs))
    for i in range(k):
        # print("Heap: {}".format(costs))
        # get the minor prime on costs
        c = heapq.heappop(costs)
        # set the prime before with c to heap!
        heapq.heappush(costs, c**2)
        # print("Pop: {} | Push: {} => n = {} * {}".format(c, c ** 2, n, c))
        n *= c
        # that way the n value is small at each iteration
        # and we calculate more faster so well
        # try remove that with the block of 'for'
        # and the time get a worse cost: 3s -> 3min!
        if modulus:
            n %= modulus

    # print("Answer: {}".format(n))
    return n


test = smallest_integer(4)
assert test == 120, "solve(4) got {}, expected 120".format(test)

if __name__ == "__main__":
    print(smallest_integer(500500, 500500507))
