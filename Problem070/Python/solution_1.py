import math
from collections import Counter

def _prime_sieve(start, limit):
    def is_prime(n):
        if n%2 == 0:
            return False
        for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n%i == 0:
                return False
        return True
    sieve = []
    if start <= 2: sieve.append(2)
    for i in range(start, limit, 2):
        if is_prime(i):
            sieve.append(i)
    return sieve

def _is_permutation(x, y):
    return Counter(str(x)) == Counter(str(y))

def min_phi_ratio(limit):
    sq = math.sqrt(limit)
    primes = _prime_sieve(math.floor(sq - sq*0.4),
                          math.floor(sq + sq*0.4))
    l = len(primes)
    min_ratio = 2
    target = None
    for p in range(0, l):
        for q in range(p, l):
            n = primes[p] * primes[q]
            if n>limit:
                break;
            phi = (primes[p] - 1) * (primes[q] - 1)
            if _is_permutation(n, phi) and n/phi < min_ratio:
                target = n
                min_ratio = n/phi
    return target

def solve():
    return min_phi_ratio(10000000)

if __name__ == "__main__":
    print(solve())
