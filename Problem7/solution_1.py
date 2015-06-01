"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from primes import primeGenEff
p = 0
for i in primeGenEff(1000000000000):
	p += 1
	if p == 10001:
		print i
		break	 