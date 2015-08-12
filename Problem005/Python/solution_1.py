"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#my ugly solution D: #brute-force:
# divisors = [x for x in xrange(1, 21)]
# x = 1
# while True:
# 	smallest = True
# 	for i in divisors:
# 		if x % i != 0:
# 			smallest = False
# 			break
# 	if smallest:
# 		print(x)
# 		break
# 	x += 1

#beatiful solution:
i = 1 
for k in (range(1, 21)): 
	if i % k > 0: 
		for j in range(1, 21): 
			if (i*j) % k == 0: 
				i *= j 
				break 
print(i)
