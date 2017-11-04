import math

def _prime_sieve(start, limit):
    def is_prime(n):
        if n%2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n%i == 0:
                return False
        return True
    sieve = []
    if start <= 2: sieve.append(2)
    for i in range(start, limit):
        if is_prime(i):
            sieve.append(i)
    return sieve

LIMIT = 50000000

s = lambda x: int(math.sqrt(x))

def solve(limit):
    numbers = {}
    primes_2 = _prime_sieve(2, s(limit))
    primes_3 = _prime_sieve(2, int(limit**(1/3))+1)
    primes_4 = _prime_sieve(2, s(s(limit))+1)
    for i in primes_2:
        for j in primes_3:
            for k in primes_4:
                n = i**2 + j**3 + k**4
                if n >= limit:
                    break
                else:
                    numbers[n] = 0
    return len(numbers)


if __name__ == "__main__":
    print(solve(LIMIT))
