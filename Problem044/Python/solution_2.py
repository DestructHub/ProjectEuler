#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Unknown Author
#
#

from itertools import count


def int_sqrt(n):
    # An integer-arithmetic variant of the Babylonian method for
    # calculating square roots.  Given a non-negative integer n, we find
    # the greatest non-negative integer k such that k*k <= n.
    #
    # Suppose k > 0 is an integer such that k*k > n.  Then
    # k + n//k < 2*k, and because 2*k is even it follows that
    # (k + n//k)//2 < k.  Furthermore,
    #
    #     (k + n/k)**2
    #         == k**2 + 2*n + (n/k)**2
    #         == k**2 - 2*n + (n/k)**2 + 4*n
    #         == (k - n/k)**2 + 4*n
    #         > 4*n
    #
    # so
    #
    #     (k + n/k)/2 > sqrt(4*n)/2 == sqrt(n)
    #         => (k + n//k)//2 >= int_sqrt(n).
    #
    # Thus, by starting with k such that k*k >= n and iteratively
    # replacing k with (k + n//k)//2 while k*k > n we will eventually
    # reach a point where k*k <= n.  At this point, it must be that
    # k == int_sqrt(n).
    #
    # k = n is a natural starting point.  Instead, we will take
    #
    #     k = 1 << -(-n.bit_length()//2)
    #
    # which is a much better initial approximation and so will result in
    # fewer iterations.  Note the use of the idiom -(-x//y) for "divide
    # x by y and round up".  Note also that
    #
    #     k*k
    #         == (1 << -(-n.bit_length()//2))**2
    #         == 1 << (-(-n.bit_length()//2))*2
    #         >= 1 << n.bit_length()
    #         > n,
    #
    # satisfying the algorithmic requirement that k*k >= n initially.
    #
    k = 1 << -(-n.bit_length()//2)
    while k*k > n:
        k = (k + n//k)//2
    return k


def pentagonal_number(n):
    return n*(3*n - 1)//2


def is_pentagonal(n):
    # If n is pentagonal then there exists k such that
    #
    #     n == pentagonal_number(k)
    #         =>  n == k*(3*k - 1)/2
    #         =>  2*n == 3*k**2 - k
    #         =>  24*n == (6*k)**2 - 12*k
    #         =>  24*n + 1 == (6*k - 1)**2
    #         =>  int_sqrt(24*n + 1) == 6*k - 1
    #         =>  (int_sqrt(24*n + 1) + 1)//6 == k
    #
    # Thus, n is pentagonal if and only if it is the kth pentagonal
    # number where
    #
    #     k = (int_sqrt(24*n + 1) + 1)//6.
    #
    k = (int_sqrt(24*n + 1) + 1)//6
    return pentagonal_number(k) == n


def answer():
    # If p[j], p[k] are two pentagonal numbers with j < k then
    #
    #    p[k] - p[j]
    #        == k*(3*k - 1)/2 - j*(3*j - 1)/2
    #        == (3*k*k - k - 3*j*j + j)/2
    #        == (3*k*k - 6*k*j + 3*j*j - k + j + 6*k*j - 6*j*j)/2
    #        == (3*(k-j)**2 - (k-j) + 6*j*(k-j))/2
    #        == p[k-j] + 3*j*(k-j).
    #
    # We are interested only in pairs (j, k) where this differences is
    # itself a pentagonal number, p[t] say.  Setting s = k - j we have
    #
    #     p[t] == p[s] + 3*j*s.
    #
    # Thus, it suffices to consider only pairs (s, t) with s < t for
    # which p[t] - p[s] is a multiple of 3*s.  Any such pair
    # automatically yields j and k such that p[k] - p[j] == p[t] leaving
    # us needing only to check that p[j] + p[k] is pentagonal.
    #
    # Because we want the minimum p[t] with the above properties, we
    # consider each s < t before moving on to t + 1.  Given the relative
    # expense of calculating (p[t] - p[s]) % (3*s) we first screen
    # candidate values of s in view of the following.
    #
    # (1) For all non-negative integers n,
    #
    #     (p[n] - n)%3
    #         == (n*(3*n - 1)/2 - n)%3
    #         == (n*(3*n - 3)/2)%3
    #         == 0
    #
    # Thus, if (p[t] - p[s]) % (3*s) == 0 then we must have that
    # (t - s)%3 == 0.
    #
    # (2) If (p[t] - p[s]) % (3*s) == 0 then
    #
    #     (p[t] - p[s]) % s == 0
    #         => (2*p[t] - 2*p[s]) % s == 0
    #         => (2*p[t] - s*(3*s - 1)) % s == 0
    #         => 2*p[t] % s == 0
    #
    p = {}
    for t in count():
        p[t] = pentagonal_number(t)
        double_p_t = 2 * p[t]
        for s in range(t - 3, 0, -3):
            if not double_p_t % s and not (p[t] - p[s]) % (3*s):
                j = (p[t] - p[s]) // (3*s)
                if is_pentagonal(p[t] + 2*pentagonal_number(j)):
                    return p[t]


print(answer())