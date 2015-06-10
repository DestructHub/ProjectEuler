"""
Digit factorials
Problem 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

f = lambda n: reduce(lambda a, b: a*b, [u for u in range(n + 1) if u != 0] + [1])
c = lambda x: sum([f(int(n)) for n in str(x)]) == x
filtred_range = lambda i: filter(lambda x: not bool(sum([int(n) for n in str(x)]) & x), range(3, i)) 
gen = lambda y: (x for x in filtred_range(y) if c(x))
g = gen(10 ** 7) #because 9!*7 < 99999999
s = sum(x for x in g)
print(s)