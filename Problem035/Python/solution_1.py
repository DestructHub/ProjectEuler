#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#


def is_prime(n):
    if n <= 3:
        return n >= 2
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


def circPrime(n):
    n1 = str(n)*2
    for i in range(len(str(n))):
        if not is_prime(int(n1[i:len(str(n))+i])):
            return False
    return True
print(len([x for x in range(1000000) if circPrime(x)]))
