#include <stdio.h>
#include <string.h>
#define max(x,y) (x)>(y)?(x):(y)
#define D 1000

int remainders[D];

int get_max_rec(int n)
{
    int times = 1,dividend = 1;
    memset(remainders, 0, D * sizeof(int));
    //printf("-----------------------------\n");
    //printf("%d\n",n);
    //printf("-----------------------------\n");
    for(; dividend!=0 ;)
    {
        //printf("%d %d\n",dividend,times);
        if (remainders[dividend])
            return times - remainders[dividend];
        remainders[dividend] = times++;
        if (dividend < n)
            dividend *= 10;
        dividend = dividend % n;
    }
    return 0;
}

int main(int argc, char *argv[])
{
    int max_rec = 0, d, d_max;
    for( d = 3 ; d < D ; d++)
    {
        int new_max_rec = get_max_rec(d);
        //printf( "%d : %d\n",d , new_max_rec(d) );
        if (new_max_rec > max_rec) {
            max_rec = new_max_rec;
            d_max = d;
        }
    }
    printf("%d\n", d_max);
    return 0;
}
