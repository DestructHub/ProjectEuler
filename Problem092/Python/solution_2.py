#coding=utf-8
"""
Square digit chains
Problem 92

A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
"""
#simple version, not optmized.
#230s+-
def sequence_end(start):
	end = start
	while end != 1 and end != 89:
		end = sum(map(lambda x: x * x, [int(x) for x in str(end)]))
	return end

total = 0
[total.__add__(1) for x in range(1, 10**7) if sequence_end(x) == 89]
print(total)