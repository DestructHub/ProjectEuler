import math
frac=1.0
for b in range(1,10):
    for a in range(1,b):
        for c in range(1,10):
            if (a*10+b)/(b*10+c)==a/c:
                frac*=(a/c)
print(math.ceil(1/frac))
