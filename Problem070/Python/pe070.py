  
#code created by NamanNimmo Gera
#9:43am, April 16, 2019.

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

def checker(n1,n2):
    N1 = [int(i) for i in str(n1)]
    N2 = [int(j) for j in str(n2)]
    N1.sort()
    N2.sort()
    if N1==N2:
        return True
    else:
        return False

def phi(n): #to calculate the number of divisors
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
mini = 100 #randomly :P
for j in range(2,10000000):
    if checker(j,phi(j)) and (j/phi(j))<mini:
        mini = j/phi(j)
        ans = j
print(ans)        
