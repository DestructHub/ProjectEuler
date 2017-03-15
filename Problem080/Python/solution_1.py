#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#    Copyright © Manoel Vilela 2017
#
#       @team: DestructHub
#    @project: ProjectEuler
#     @author: Manoel Vilela
#      @email: manoel_vilela@engineer.com
#

import decimal
import math


def solution(limit):
    decimal.getcontext().prec = 102  # more than 100 to avoid round errors
    result = 0
    for n in range(limit + 1):
        if not math.sqrt(n).is_integer():  # check if is irrational
            # sum digits
            result += sum(decimal.Decimal(n).sqrt().as_tuple()[1][:100])

    return result


if __name__ == '__main__':
    print(solution(100))
