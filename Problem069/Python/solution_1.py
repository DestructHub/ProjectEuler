import math

def is_prime(n):
    if n%2 == 0:
        return False
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n%i == 0:
            return False
    return True

def max_phi_ratio(n):
    k = 3
    prod = 2
    while k * prod <= n:
        if is_prime(k):
            prod *= k
        k += 2
    return prod

def solve_problem_069():
    return max_phi_ratio(1000000)

if __name__ == "__main__":
    print(solve_problem_069())
