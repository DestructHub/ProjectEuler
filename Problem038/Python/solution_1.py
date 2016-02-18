#!/usr/bin/env python
# coding=utf-8
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

from collections import Counter


class PanDigital(int):

    dig = ''
    iteration = 1

    def map(self, x):
        return str(self * x)

    def concat(self, digits):
        return self.dig + digits

    @property
    def can_continue(self):
        return len(self.dig) < 10 and self.count

    @property
    def count(self):
        return all(False for x in Counter(self.dig).values() if x > 1)

    @property
    def sorted(self):
        return ''.join(map(str, sorted(map(int, self.dig))))

    @property
    def ispandig(self):
        return self.sorted == '123456789'

    def transform(self):
        while self.can_continue:
            self.dig = self.concat(self.map(self.iteration))
            if self.ispandig:
                return self.dig
            self.iteration += 1

        return None

    @property
    def value(self):
        v = self.transform()
        if v is not None:
            return int(v)
        return None

p = PanDigital
print(max(p(x).value for x in range(10000) if p(x).value))
