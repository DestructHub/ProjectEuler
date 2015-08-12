#coding=python
"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""
#1 +3 + 5 + 7 + 9 = 25
#24 + 25 + 13 + 17 + 21 = 101
#669171001

d = lambda x: x * x
r = lambda x: (num for num in range(d(x) -(3)*(x-1), d(x) +1, x - 1))                            
t = sum(sum(i)for i in range(3, 1001 + 1, +2)) + 1
print(t)


