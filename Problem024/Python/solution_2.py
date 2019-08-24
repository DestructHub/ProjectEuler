#code created by NamanNimmo Gera
#12:42pm, April 10, 2019.

from itertools import permutations

perm = permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
for count, item in enumerate(perm):
    #to find the millionth permutation
    if count == 999999:
        tup_join = item;
        str_join = "".join(str(x) for x in tup_join)
        print(str_join);
        break;                    
