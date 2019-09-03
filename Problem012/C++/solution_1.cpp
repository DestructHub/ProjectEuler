#include<bits/stdc++.h>
using namespace std;
#define MAX 1000000000
#define LL long long int
LL countDivisors(LL n)
{
    LL cnt = 0;
    for (int i = 1; i <= sqrt(n); i++) {
        if (n % i == 0) {
            if (n / i == i) cnt++;
            else cnt+=2;
        }
    }
    return cnt;
}
int main()
{
    LL i;
    for(i=1;i<MAX;i++)
    {
       LL a = (i*(i+1))/2;
       LL k = countDivisors(a);
       if(k>500)
       {
           printf("%lld\n",a);
           break;
       }
    }
    return 0;
}
