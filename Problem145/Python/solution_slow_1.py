#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
How many reversible numbers are there below one-billion?
Problem 145

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. 
For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""
from functools import reduce
from itertools import permutations, combinations_with_replacement


def other_function(n):
    for i in xrange(11, n):
        if str(i)[0] == '0' or str(i)[-1] == '0':
            continue
        yield i

    # combs = reduce(list.__add__, [[(x, y) for y in range(0, 10) if (x ^ y) & 1 and not (x == 0 or y == 0)] for x in range(0, 10)])
    # for comb in combs:
    #   start, end = comb
    #   num = int(str(start) + str(end))
    #   yield num

    # for i in range(n):
    #   for comb in combs:
    #       start, end = comb
    #       num = int(str(start) + str(i) + str(end))
    #       if num > n:
    #           break
    #       yield num
            



def gen_filtred(n, start = 1): #n - potencia de 10
    #combinações de números possíveis simetricamente
    combs = reduce(list.__add__, [[(x, y) for y in range(0, 10) if (x ^ y) & 1] for x in range(0, 10)])
    exp = start
    while exp < n:
        tamanho = len(str(10 ** exp))//2
        if exp & 1 == 1: #expoente impar na base 10 -> tamanho par
            for comb in combinations_with_replacement(combs, tamanho):
                for perm in set(permutations(comb)):
                    first = perm[0]
                    head, tail = first
                    if head == 0 or tail == 0:
                        continue
                    index = exp
                    newnum = 0
                    for mostnum, lessnum in perm:
                        newnum += mostnum * 10 ** index + lessnum * 10 ** abs(index - exp)
                        index -= 1
                    yield newnum
        else: #expoente par na base 10 -> tamanho impar 
            for comb in combinations_with_replacement(combs, tamanho):
                for perm in set(permutations(comb)):
                    first = perm[0]
                    head, tail = first
                    if head == 0 or tail == 0:
                        continue
                    for middle in range(10):
                        #print('Comb: {}| Perm: {}'.format(comb, perm))
                        index = exp
                        newnum = middle * 10 ** (exp // 2)
                        for mostnum, lessnum in perm:
                            newnum += mostnum * 10 ** index + lessnum * 10 ** abs(index - exp)
                            index -= 1
                        yield newnum
        exp += 1

def sumreverse(num):
    return str((int(str(num)[::-1]) + num))
def reversible(num):
    return reduce(lambda a, b: a*b, [int(y) for y in sumreverse(num)]) & 1


range_x = lambda x: gen_filtred(len(str(x)) - 1)
range_y = lambda y: other_function(y)


test = 10 ** 9
print('Testando até: %s ' %test)
gen_list = []
total = 0
for i in range_x(test):
    #print(i)
    if reversible(i) == 1:
        #print('%d + %s = %s' %(i,  str(i)[::-1], sumreverse(i)))
        total += 1
        #gen_list.append(i)
        #print(total)
    #else:
        #print('Não é reversível: %s' %i)
print('Total range_x: %d' %total)

#Usado para testes
# other_list = []
# total = 0
# for i in range_y(test):
#   if reversible(i) == 1:
#       #print('%d + %s = %s' %(i,  str(i)[::-1], sumreverse(i)))
#       total += 1
#       other_list.append(i)
#       #print(total)
#   #else:
#       #print('Não é reversível: %s' %i)
# print('Total range_y: %d' %total)
for gen, other in zip(gen_list, other_list):
    if gen not in other_list:
        print('A função other não está gerando o reversível: ' %gen)
    if other not in gen_list:
        print('A função gen_filtred não está gerando o reversível: ' %other)