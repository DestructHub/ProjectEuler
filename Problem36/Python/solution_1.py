def isPal(n):
    return str(n) == str(n)[::-1]
def binDecPal(x):
    if isPal(x):
        n = bin(x)[2:]
        if isPal(n):
            return True
    return False
print(sum([x for x in range(1000000) if binDecPal(x)]))