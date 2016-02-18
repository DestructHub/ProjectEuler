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
from string import ascii_lowercase as alf
from random import sample
#from kbhit_unix import KBHit as kbhit
phi = ((1+sqrt(5))/2)

def gen(x, sign = 1, start = 0, reverse = False):
	if not reverse:
		i = start
		while i < x:
			i += 1
			yield i * sign
	else:
		while x > start:
			x -= 1
			yield x * sign

def phi_index(n, resto = 0, lista = []):
	if resto == 0:
		resto = n

	last = 0
	for i in gen(n):
		if phi ** i > resto:
			lista.append(last)
			break
		last = i

	resto -= phi ** last
	if resto <= 1:
		if resto != 0:
			return suf_phi(n, resto, lista)
		else:
			return lista
	else:
		return phi_index(n, resto, lista)

def suf_phi(n, resto = 0, lista = []):
	if resto == 0:
		resto = n

	last = -n
	for i in gen(n, sign = -1, start = -1, reverse = True):
		if phi ** i - 0.000001 > resto:
			lista.append(last)
			break
		last = i

	resto -= phi ** last
	if resto <= 0.000001:
		return lista
	else:
		return suf_phi(n, resto, lista)

def phibase(n):
	index = phi_index(n, lista = [])
	msb = max(index); lsb = min(index)

	#Inicializar string a direita (prefixa)
	pre = []
	for i in range(msb + 1):
		pre.append('0')

	#Inicializar string a esquerda (sufixa)
	suf = []
	for i in range(abs(lsb)):
		suf.append('0')

	for i in index:
		if i >= 0:
			pre[i] = '1'
		else:
			suf[~i] = '1'

	return ''.join(pre[::-1]) + '.' + ''.join(suf)

def calc(index):
	_sum_ = 0
	for i in index:
		_sum_ += phi ** i

	if _sum_ + 0.0001 >= int(_sum_):
		return int(_sum_)
	else:
		return _sum_

def intphi(phinum):
	point = phinum.find('.')
	pre, suf = phinum[:point][::-1], phinum[point + 1:]
	index = []
	for i in range(len(pre)):
		if pre[i] == '1':
			index.append(i)
	for i in range(len(suf)):
		if suf[i] == '1':
			index.append(~i)


	return calc(index)

def gen_palindromic(n):
	pass

def palindromic(string):
	if string != None:
		return string == string[::-1]

test = 10 ** 10  #last: 6
num = phibase(test)
with open('test' +'/'+ 'p473_' + ''.join(sample(alf, 8)) + '.txt', 'x') as f:
	f.write(num)