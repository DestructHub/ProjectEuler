#!/usr/bin/env python3
#coding=utf-8
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
#hahahhahaha!! consegui: answer 608720
#Demorou pra caramba, tem que melhorar ainda... mas funciona!


combs = reduce(list.__add__, [[(x, y) for y in range(0, 10) if (x ^ y) & 1 or (x + y) < 10] for x in range(0, 10)])

def sumreverse(num):
	return str((int(str(num)[::-1]) + num))
def reversible(num):
	return bool(reduce(lambda a, b: a*b, [int(y) for y in sumreverse(num)]) & 1)

def gen_filtred(n, start = 1): #n - potencia de 10
	exp = start
	while exp < n:
		tamanho = (exp + 1)//2
		#expoente impar na base 10 -> tamanho par
		for comb in combinations_with_replacement(combs, tamanho):
			for perm in sorted(set(permutations(comb))):
				head, tail = perm[0]
				if head == 0 or tail == 0 or not bool((head + tail) & 1):
					continue
				if exp & 1 == 1:
					index = exp
					newnum = 0
					for leftnum, rightnum in perm:
						newnum += (leftnum * 10 ** index) + (rightnum * 10 ** abs(index - exp))
						index -= 1
					yield newnum
				else:
					for middle in range(10):
						index = exp
						newnum = middle * 10 ** (index // 2)
						for leftnum, rightnum in perm:
							newnum += (leftnum * 10 ** index ) + (rightnum * 10 ** abs(index - exp))
							index -= 1
						yield newnum
		exp += 1


range_x = lambda x: gen_filtred(len(str(x)) - 1)

test = 100000000
print('Testando até: %s ' %test)
total = 0
for i in range_x(test):
	print(i)
	if reversible(i):
		total += 1

print('Total: %d' %total)

