#code created by NamanNimmo Gera
#9:06am, April 16, 2019.

MAX = 1000001
p = []
def sieve():  
    isPrime = [0] * (MAX + 1);  
    for i in range(2, MAX + 1):  
        if (isPrime[i] == 0):  
            p.append(i)
            j = 2 
            while (i * j <= MAX):  
                isPrime[i * j]= 1; 
                j += 1 

def phi(n): 
    res = n
    i = 0
    while (p[i] * p[i] <= n):  
        if (n % p[i]== 0):  
            res -= int(res / p[i])
            while (n % p[i]== 0): 
                n = int(n / p[i]) 
        i += 1
    if (n > 1): 
        res -= int(res / n)
    return res  

sieve()
nbyCount = 1
maxi = 1
for j in range(2,1000001):
    if (j/phi(j))>nbyCount:
        nbyCount = (j/phi(j))
        maxi = j
    
print(maxi)
