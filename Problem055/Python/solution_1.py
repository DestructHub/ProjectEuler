#code created by NamanNimmo Gera
#4:57pm, May 1, 2019.

def reverse(x):
    return int(str(x)[::-1])

def Palindrome(x):
    if x == reverse(x):
        return True
    else:
        return False

#function to check if a number is a Lychrel number or not
def checkLyr(x):
    tot = 0
    while True:
        x  = x + reverse(x)
        if Palindrome(x):
            return False
        else:
            tot = tot + 1
        if tot>50:
            return True
        
count = 0
for i in range(1,10000):
    if checkLyr(i):
        count = count + 1
print(count)        
    
