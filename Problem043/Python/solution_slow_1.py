
#code created by NamanNimmo Gera
#2:21pm, April 18, 2019.

from itertools import permutations

perm = permutations([0,1,2,3,4,5,6,7,8,9])
prime_list = [2,3,5,7,11,13,17]
tot=0

for i in list(perm):
    prime = 0
    flag = 1
    for j in range(1,8):
        string = ""
        string = string + str(i[j]) + str(i[j+1]) + str(i[j+2])
        if int(string)%(prime_list[prime]) != 0:
            flag = 0
            break
        else:
            prime = prime + 1
    if flag == 1:
        tot = tot + int(''.join(map(str, i)))
print(tot)
