#include <stdio.h>
#include <stdlib.h>
int main()
{
    unsigned long int m=0,n=0, palindrome=0,h;
    int i=0,j=0;
    for(i=100;i<=999;++i)
    {
        for(j=100;j<=999;++j)
        {
            int a=0;
            m=0;n=0;
            m=i*j;
            n=m;
            h=0;
            while(m!=0)
            {
                a=m%10;
                m=m/10;                
                h=h*10 +a;
            }
            if(h==n && h>=palindrome)
            palindrome=h;
        }
    }
    printf("%d",palindrome);
    return 0;
}
