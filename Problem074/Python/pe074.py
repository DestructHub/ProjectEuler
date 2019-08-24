import math
#start = time.time()
tot=0
for i in range(1,1000000+1):
    newlist = []
    j = i
    while(j not in newlist):
        newlist.append(j)
        j = sum(math.factorial(int(i)) for i in str(j))
    if len(newlist)==60:
        tot += 1
#end = time.time()
print(tot) 
