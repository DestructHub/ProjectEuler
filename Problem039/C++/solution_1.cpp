#include <stdio.h>

int i,j,k;
int MAX=1000;
int Ps[1001];
int maxP;
 
 
int main()
{
	for(i=1;i<=MAX;i++)
	{
		for(j=i;j<=MAX;j++)
		{
			for(k=j;k*k<(i*i+j*j);k++);
			if( i*i+j*j == k*k && i+j+k<=MAX )
			{
				//printf( "%d %d %d %d\n",i,j,k,i+j+k );
				Ps[i+j+k]++;
			}
		}
	}
	for(i=1;i<=MAX;i++)
	{	
		if( Ps[maxP] < Ps[i] )
			maxP = i;
	}
	printf("%d\n",maxP);
    return 0;
}
