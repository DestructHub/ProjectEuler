#code created by NamanNimmo Gera
#3:31pm, April 12, 2019.

import math

def findsum(n):
    smallsum = 0
    while(n>0):
        smallsum = smallsum + math.factorial(n%10)
        n = n//10
    return(smallsum)    

tot = 0
for i in range(10,50000): #see why this upper bound is being chosen ;)
    if findsum(i)==i:
        tot = tot + i
print(tot) #145+40585
