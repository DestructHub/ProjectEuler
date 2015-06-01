#coding=utf-8
"""

Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

"""
from string import digits
def factorial(n):
	if n < 1: return 1
	else: return n * factorial(n - 1)

#seja a entrada o número element do elemento ordenado e a lista ordenada de elementos
def problem24(element, nums = list(digits)):
	answer = ''
	while len(nums) != 0:
		#calcula a periodicidade da casa unitária atual
		factor_num = factorial(len(nums) - 1)
		#verifica qual deve ser o número da casa atual
		if element % factor_num == 0:
			order = element//factor_num 
		else:
			order = element//factor_num + 1
		#fica apenas com o resto da periodicidade, que nos diz qual número é
		order %= len(nums)
		#insere o valor na string final
		answer += nums.pop(order - 1)

	return answer

print(problem24(10 ** 6))



