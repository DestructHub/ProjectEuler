#coding=utf-8
"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a² + b² = c²

For example, 3² + 4² = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""

def decompSum(n):
	maxRange = n // 2 # i want to break free (queen)
	#from euclids formula, its possible proof the a and b its multiples to 3-4 and c multiple 5
	range_a_or_b = filter(lambda x: x % 3 == 0 or x % 4 == 0 or x % 5 == 0, range(1, maxRange))
	range_c = filter(lambda x: x % 5 == 0, range_a_or_b)
	for a in range_a_or_b:
		for b in range_a_or_b:
			for c in range_c:
				if a + b + c == n and a != b != c:
					yield sorted((a, b, c))

def pythagorean(a, b, c):
	return (a ** 2 + b ** 2) == c ** 2

def problem9(n):
	for a, b, c in decompSum(n):
		if pythagorean(a, b, c):
			print '%d² + %d² = %d² (%d)' %(a, b, c, a + b + c)
			print '%d * %d * %d = %d' %(a, b, c, a*b*c)
			return	

problem9(1000)

# out:
#200² + 375² = 425² (1000)
#200 * 375 * 425 = 31875000

# out:
#200² + 375² = 425² (1000)
#200 * 375 * 425 = 31875000