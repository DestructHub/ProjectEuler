#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#


def fib_generator(n):
    a, b = 1, 1
    while b <= n:
        a, b = b, a + b
        yield a


def solution(n):
    return sum(i for i in fib_generator(n) if not i % 2)

if __name__ == '__main__':
    print(solution(4000000))
