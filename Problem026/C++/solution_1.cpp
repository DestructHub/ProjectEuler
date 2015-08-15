#include <stdio.h>
#include <string.h>
#define max(x,y) (x)>(y)?(x):(y)
#define D 1000
 
int remainders[D+2];
 
int get_max_rec( int n )
{
    int time=1,dividend=1;
    memset(remainders,0,(D+2)*sizeof(int));
    //printf("-----------------------------\n");
    //printf("%d\n",n);
    //printf("-----------------------------\n");
    for(; dividend!=0 ;)
    {   
        //printf("%d %d\n",dividend,time);  
        if( remainders[dividend] )
            return time - remainders[dividend];
        remainders[dividend] = time++;
        if(dividend<n)
            dividend*=10;
        dividend = dividend%n;
    }
    return 0;
}
 
int main()
{
    int max_rec = 0,d;
    for( d=2 ; d<D ; d++ )
    {
        //printf( "%d : %d\n",d , get_max_rec(d) );
        max_rec = max( get_max_rec(d) , max_rec );
    }
    printf("%d\n",max_rec);
    return 0;
}
