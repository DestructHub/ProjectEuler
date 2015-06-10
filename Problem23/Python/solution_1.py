"""

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""
from functools import reduce
from itertools import combinations_with_replacement as combinations
max_num = 28123

def divisors(num):
	return set(reduce(list.__add__, [[div, num//div] for div in range(2, int(num**0.5) + 1) if num % div == 0] + [[1]]))

def abundant(num):
	return sum(divisors(num)) > num

abundant_nums = (n for n in range(1, max_num) if abundant(n))
sum_of_two_abundants = set(a + b for a, b in combinations(abundant_nums, 2))
not_abundant_nums = (x for x in range(max_num) if x not in sum_of_two_abundants)
print(sum(not_abundant_nums))


