#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

print(sum(map(lambda x: x ** x, range(1, 1000))) % 10 ** 10)
