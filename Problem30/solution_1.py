#coding=utf-8
"""
Digit fifth powers
Problem 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
""" Prova de um cara lá no fórum do PE sobre apenas ser necessário considerar números de 6 dígitos ou menos.
Proof that one need only consider numbers 6 digits or less:  
If N has n digits, then 10^{n-1} <= N.  
If N is the sum of the 5th powers of its digits, N <= n*9^5.  Thus, 10^{n-1} <= n*9^5.

We now show by induction that if n>=7, then 10^{n-6} > n.
1) Basis step (n=7):  10^{7-6} = 10 > 7.
2) Induction step:  suppose 10^{n-6} > n for some n>=7.  Show this true for n+1 too.  Well,
     10^{(n+1)-6} = 10*10^{n-6} > 10n > 2n > n+1
QED.

It follows that if n>=7, then 
     10^{n-1} = 10^{n-6}*10^5 > n * 10^5 > n*9^5.  

Hence the only way we can have 10^{n-1} <= n*9^5 is for n<=6.  
"""

#Aqui foi pura sorte.
#Inicialmente tentei pensar num limite para testes, seria o tamanho*9**5, mas não consegui deduzir o maior tamanho possível
#Desse jeito, fiz alguns testes e descobri que a ocorrência de números que poderiam ser escritos como a soma de potência(5)
#Era no tamanho intervalo de [4, 7)
from itertools import combinations_with_replacement as c; from string import digits as d
n = lambda num, digits: sorted(str(num)) == sorted(digits)
p = lambda comb: sum([int(n) ** 5 for n in comb])
print(sum(set(reduce(list.__add__, ([p(cb) for cb in c(d, x) if n(p(cb), cb)] for x in range(7))))))