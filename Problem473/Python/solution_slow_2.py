# -*- coding: utf-8 -*-
#problem 473
"""
Let φ be the golden ratio: φ=1+5√2.
Remarkably it is possible to write every positive integer as a sum of powers of φ even if we require that every power of φ is used at most once in this sum.
Even then this representation is not unique.
We can make it unique by requiring that no powers with consecutive exponents are used and that the representation is finite.
E.g: 2=φ+φ^-2 and 3=φ^2+φ^-2

To represent this sum of powers of φ we use a string of 0's and 1's with a point to indicate where the negative exponents start.
We call this the representation in the phigital numberbase.
So 1=1φ, 2=10.01φ, 3=100.01φ and 14=100100.001001φ.
The strings representing 1, 2 and 14 in the phigital number base are palindromic, while the string representating 3 is not.
(the phigital point is not the middle character).

The sum of the positive integers not exceeding 1000 whose phigital representation is palindromic is 4345.

Find the sum of the positive integers not exceeding 10^10 whose phigital representation is palindromic. 

"""
from math import *
from kbhit_unix import KBHit as kbhit
phi = ((1+sqrt(5))/2)


def phi_pre_gen(n):
	resto = n
	while resto >= 1:
		last = 0
		for i in xrange(n):
			if phi ** i > resto:
				break
			last = i
		resto -= phi ** last
		yield last
	yield resto
def phi_suf_gen(n, resto):
	while resto >= 0.0001:
		last = -n
		for i in xrange(-n, -1):
			if phi ** i - 0.0001 > resto:
				break
			last = i
		resto -= phi ** last
		yield last
def checkpal(n):
	if n == 1:
		return True

	pre = [x for x in phi_pre_gen(n)]
	pre, resto = pre[:-1], pre[-1]
	suf = [x for x in phi_suf_gen(n, resto)]

	for i in xrange(len(pre)):
		try:
			if pre[i] != ~suf[~i]:
				return False
		except IndexError:
			return False
	return len(pre) == len(suf)



sum = 0
kb = kbhit()
total = 10 ** 10
for i in xrange(total):
	if checkpal(i):
		sum += i
	if kb.kbhit() and kb.getch():
		print 'Atual: %*s / %d | %4.2f %% | Sum: %d' %(len(str(total)), str(i), total, i * 100 / total,  sum)
print sum
