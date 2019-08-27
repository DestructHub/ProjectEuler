#code created by NamanNimmo Gera
#11:22pm, April 13, 2019.

triangular_list = []
pentagonal_list = []
hexagonal_list = []
for i in range(1,100000):
    triangular_list.append(int((i*(i+1))/2))
    pentagonal_list.append(int((i*(3*i-1))/2))
    hexagonal_list.append(int(i*(2*i-1)))

for i in triangular_list:
    if i in pentagonal_list:
        if i in hexagonal_list:
            if i>40755:
                print(i)
                break
