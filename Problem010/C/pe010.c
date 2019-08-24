//created by NamanNimmo 
//7:17 pm, april 8, 2019.

#include <stdio.h>
#include <math.h>

#define n 2000001

int main()
{
   long long int i,j,sum;
   static int primes[n];
   i=0;j=0;sum=0;
   // I have used sieve of erastosthenes.
   for(i=0;i<n;i++)
   {
       primes[i]=1;
   }
   for(i=2;i<sqrt(n);i++)
   {
       if(primes[i]==1)
       {
           for(j=i;j*i<n;j++)
           {
               primes[i*j]=0;
           }
       }
   }
   for(i=2;i<n;i++)
   {
       if(primes[i]==1)
         sum += i;
   }
   printf("%lld",sum);
    return 0;
}
