#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © 2019 Manoel Vilela
#
#    @project: Project Euler
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

"""
Working from left-to-right if no digit is exceeded by the digit to its
left it is called an increasing number; for example, 134468.

Similarly if no digit is exceeded by the digit to its right it is
called a decreasing number; for example, 66420.

We shall call a positive integer that is neither increasing nor
decreasing a "bouncy" number; for example, 155349.

Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact,
the least number for which the proportion of bouncy numbers first
reaches 50% is 538.

Surprisingly, bouncy numbers become more and more common and by the
time we reach 21780 the proportion of bouncy numbers is equal to 90%.

Find the least number for which the proportion of bouncy numbers is
exactly 99%.
"""


def bouncy(num: int) -> bool:
    digits = str(num)
    comparisons = set()

    for d1, d2 in zip(digits, digits[1:]):
        if d1 == d2:
            continue
        state = 1 if int(d1) > int(d2) else 0
        comparisons.add(state)
        if len(comparisons) == 2:
            return True

    return False


def bouncy_counter(threshold: float):
    bouncy_numbers = 0
    n = 100
    percentage = 0
    while percentage < threshold:
        n += 1
        if bouncy(n):
            bouncy_numbers += 1
        if bouncy_numbers > 0:
            percentage = bouncy_numbers / n
    return n


def main():
    print(bouncy_counter(0.99))


if __name__ == '__main__':
    main()
