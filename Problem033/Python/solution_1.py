#!/usr/bin/env python
#
#   Python Script
#
#   Copyright © Manoel Vilela
#
#

limit = 100


def mdc(a, b):
    if (b == 0):
        return a
    else:
        return mdc(b, a % b)


class fraction(object):

    def __init__(self, x, y):
        self.num = x
        self.den = y
        self.factored = False

    def __repr__(self):
        return '{}/{}'.format(self.num, self.den)

    def __mul__(self, frac):
        self.num *= frac.num
        self.den *= frac.den

        return self

    __rmul__ = __mul__

    @property
    def mfact(self):
        a, b = self.num, self.den
        for x in self.cross:
            self.factored = True
            a = self.new(self.num, x)
            b = self.new(self.den, x)
        d = mdc(a, b)
        return (a // d, b // d)

    @property
    def cfact(self):
        return (self.num // self.mdc, self.den // self.mdc)

    @property
    def fact(self):
        return fraction(*self.cfact)

    @property
    def mdc(self):
        return mdc(self.num, self.den)

    def new(self, w, z):
        v = ''.join([x for x in str(w) if x != z])
        if len(v) > 0:
            return int(v)
        else:
            return -1

    def get(self, num):
        return set(str(num))

    @property
    def cross(self):
        return self.get(self.num) & self.get(self.den)

    @property
    def nums(self):
        return (self.num, self.den)

    @property
    def non_trivial(self):
        nzeronegative = all(False for x in self.nums if x < 1)
        nontrivial = all(False for x in self.nums if x % 10 == 0)
        return nzeronegative and nontrivial and self.factored

    @property
    def curious(self):
        return self.non_trivial and (self.mfact == self.cfact)


def solution():
    from functools import reduce
    fracs = []
    for up in range(limit):
        for down in range(limit):
            if up < down:
                f = fraction(up, down)
                f.mfact
                if f.curious:
                    fracs.append(f)

    return reduce(lambda x, y: x * y, fracs).fact.den

if __name__ == '__main__':
    print(solution())
