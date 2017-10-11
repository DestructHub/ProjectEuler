import math

def is_prime(n):
    if n%2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True


class Problem058(object):


    def __init__(self):
        self.nprimes = 8
        self.level = 7
        self.prime_ratio = 0.62

    def _diag_primes(self):
        # Count primes on top left 3 corners
        # 3n - k(n + 1) / k => {1, 2, 3}
        return [is_prime(self.level**2 - self.level + 1),
                is_prime(self.level**2 - 2*self.level + 2),
                is_prime(self.level**2 - 3*self.level + 3)].count(True)

    def _record_next_diag_primes(self):
        self.level += 2
        self.nprimes += self._diag_primes()
        self.prime_ratio = self.nprimes / (self.level * 2 - 1)

    def _solve(self, ratio_limit):
        while self.prime_ratio > ratio_limit:
            self._record_next_diag_primes()
        return self.prime_ratio, self.level

    @classmethod
    def solve(cls):
        obj = object.__new__(cls)
        obj.__init__()
        return obj._solve(0.1)


if __name__ == "__main__":
    print(Problem058.solve())
