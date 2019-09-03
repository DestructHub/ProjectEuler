from collections import Counter

def isPrime(n) : 
    if (n <= 1) : 
        return False                #this is my brute force approach, if  I see a better solutionin the PE forum, will edit this :)
    if (n <= 3) :                   # EDIT: A much better approach: https://www.xarg.org/puzzle/project-euler/problem-41/
        return True
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
    return True
    
def checker(a): #function to check if the number has zero in it or not
    for i in str(a):
        if str(i)=='0':
            return 1
    return 0       

def repeatCheck(a): #function to check if there is any repeating digit or not
    c = Counter(str(a))
    if any(value > 1 for value in c.values()):
        return 1
    else:
        return 0

highest = 0
for j in range(1000000,10000000): #the highest number below 1million is 4231
    if isPrime(j) and (checker(j)==0) and (repeatCheck(j)==0):
        a = len(str(j))
        k = (a*(a+1))/2
        if sum(int(digit) for digit in str(j))==k:
            if j>highest:
                highest = j
print(highest)            
        
