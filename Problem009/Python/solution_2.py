#code created by NamanNimmo Gera
#11:32am, April 30, 2019.

for i in range(1,1000):
    for j in range(i+1,1000):
        k = 1000 - i - j
        if i ** 2 + j ** 2 == k ** 2: break
    if i**2 + j**2 == k**2: break

print(i*j*k)
