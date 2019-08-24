#code created by NamanNimmo Gera
#11:29am, April 14, 2019.

def isPrime(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True

def checkLeft(n):
    num = n
    while(num>0):
        if isPrime(num):
            num = num // 10
        else:
            return False
    return True
    

def checkRight(n):
    a = str(n)
    for i in range(1,len(a)):
        if isPrime(int(a[i:])):
            continue
        else:
            return False
    return True
    
tot=0
prime_list = []
for i in range(11, 1000000):
    if isPrime(i):
        prime_list.append(i)

for j in prime_list:
    if checkRight(j) and checkLeft(j):
        tot = tot + j
        
print(tot)        
