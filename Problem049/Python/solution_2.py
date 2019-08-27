#code created by NamanNimmo Gera
#12:28pm, April 19, 2019.

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

for i in range(1001,3338):
    if isPrime(i) and isPrime(i+3330) and isPrime(i + 2*3330):
        if set(list(str(i))) == set(list(str(i+3330))) == set(list(str(i + 2*3330))):
            if i!=1487:
                string = ""
                string = string + str(i) + str(i+3330)+ str(i + 2*3330)
                print(string)
                exit()
