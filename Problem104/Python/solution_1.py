import math
import decimal

# https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression

sqrt = math.sqrt
dec = decimal.Decimal

def _is_pandigital(elem):
    return [str(i) for i in range(1, 10)] == sorted(list(elem))

_PHI = dec((1 + sqrt(5))/2)
_PSI = dec(1 - _PHI)

def _fermat_approximation(n):
    return (_PHI**dec(n) - _PSI**dec(n))/dec(sqrt(dec(5)))

def _n_digit_of_decimal(d):
    s = str(d)
    return s[0] + s[2:10]

def solve():
    fa, fb, fc, t = 1, 1, 2, 2
    while 1:
        t+=1
        fc = (fa + fb) % 10 ** 9
        fa = fb
        fb = fc
        if _is_pandigital(str(fc)):
            s_top = _n_digit_of_decimal(_fermat_approximation(t))
            if _is_pandigital(s_top):
                return t

if __name__ == "__main__":
    print(solve())
