//code created by NamanNimmo Gera
//9:02 pm, April 9, 2019.

#include <bits/stdc++.h>
using namespace std;
#define LL long long int

int main()
{
    LL sum = 0;
    LL p, q;
    for (LL i = 1001;i>1;i= i-2)
    {
        p = i * i; q = i-1;
        sum += (4*p)-(6*q); 
        // (4*p - 6*q) = p +  p-q  +  p-2*q  +  p-3*q
        //simple and sweet :)
    }
    printf("%lld\n",sum+1);
    return 0;
}
