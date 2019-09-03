#code created by NamanNimmo Gera
#2:34pm, April 15, 2019.

from math import log10
count = 0
for i in range(1,10):
    count = count + int(1/(1-log10(i))) ##realise that for x > 10, x^n > 10^n
print(count)
