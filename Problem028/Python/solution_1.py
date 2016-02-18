#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a
clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a
1001 by 1001 spiral formed in the same way?
"""

# 1 +3 + 5 + 7 + 9 = 25
# 24 + 25 + 13 + 17 + 21 = 101
# 669171001

# LOOOOOOOOOOOOOOOOOOOOL, try understand this! I don't believe I wrote that...
# the worse part is the solutions are right!
black = lambda x: (num for num in range(x * x - 3 * (x - 1), x * x + 1, x - 1))
magic = sum(sum(black(i))for i in range(3, 1001 + 1, + 2)) + 1
print(magic)
