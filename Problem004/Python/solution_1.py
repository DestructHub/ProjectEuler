#!/usr/bin/env python
# coding=utf-8
#
#   Python Script
#
#   Copyleft © Manoel Vilela
#
#

from sys import version_info

if version_info >= (3, 0):
    xrange = range


"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
palindrome = 0
for i in xrange(1000):
    for j in xrange(999, 1,  -1):
        string = str(i*j)
        if string == string[::-1]:
            if palindrome < i * j:
                palindrome = i * j
                break

print(palindrome)