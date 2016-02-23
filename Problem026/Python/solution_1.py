#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

# A unit fraction contains 1 in the numerator.
# The decimal representation of the unit fractions
# with denominators 2 to 10 are given:

#     1/2   =  0.5
#     1/3   =  0.(3)
#     1/4   =  0.25
#     1/5   =  0.2
#     1/6   =  0.1(6)
#     1/7   =  0.(142857)
#     1/8   =  0.125
#     1/9   =  0.(1)
#     1/10  =  0.1

# 0.142857... = x
# 0.142857... * 1000000 = 1000000x
# 142857.142857... -0.142857... = 1000000x - x
# 142857 = 999999x
# x = 142857/999999


# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle.
# It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest
# recurring cycle in its decimal fraction part.

# replicação crua do algoritmo de divisão
# manualmente, aplica uma memória dos divisores já efetuados
# quando resto da divisão chegar num ponto onde se repete
# retorna a quantidade de divisões menos a quantidade de vezes
# que se repetiu

# Exemplo     [1/7]
#
#    10    |7
#     30   |_______
#      28  0,(1434851)...
#       20
#       14
#        60
#        56
#         40
#         35
#          50
#           49
#           (1) <= chegou ao remainder
# retorna a função menos o número de iterações.
# para o último dividendo
# se resto for zero, retorna zero, pois não há recurring cycle
# exemplos: 1/2, 1/4, 1/8

# only odd numbers need to be compute
def get_rec_cycle(n):
    """1/x get the max abc recurring cycle length of 0.(abc) num"""

    dividend, times = 1, 1
    remainder = [0 for x in range(n + 1)]
    while dividend != 0:
        times += 1
        if (remainder[dividend]):
            return times - remainder[dividend]

        remainder[dividend] += times
        if dividend == 0:
            break
        if dividend < n:
            dividend *= 10
        dividend %= n

    return 0


def get_max_rec(limit):
    return max([x for x in range(3, limit, 2)], key=get_rec_cycle)

test = get_rec_cycle(7)
assert test == 6, "Some wrong; got {},  expected 6.".format(test)

if __name__ == '__main__':
    print(get_max_rec(1000))
