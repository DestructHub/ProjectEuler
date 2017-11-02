
LIMIT = 2000000;

def solve(limit):
    a = 0
    dam = limit
    for i in range(2, 101):
        for j in range(i, 101):
            d = abs(i*(i + 1) * j*(j + 1)/4 - limit)
            if d < dam:
                a, dam = i * j, d
    return a

if __name__ == "__main__":
    print(solve(LIMIT))
