// created by NamanNimmo
//7:25 pm, April 8, 2019.

//digit fifth powers PE
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define LL long long int
#define MAX 10000000

LL fifthPowerSum(LL i){
    LL sum = 0;
    int number;
    while(i != 0){
        number = i%10;
        sum += number*number*number*number*number;
        i = i/10;
    }
    return sum;
}

int main()
{   
    int i;
    LL bigsum =0;
    for(i=2;i<MAX;i++){
        if(i == fifthPowerSum(i))
          bigsum += i;
    }
    printf("%lld\n",bigsum);
    return 0;
}
