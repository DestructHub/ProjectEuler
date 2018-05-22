#include <stdio.h>
 
int main()
 {
	int fact=1,m,i,n,j,temp,sum=0,sum1=0;
	for(i=3;i<1000000;++i)
	{
		temp=i;
		n=i;
		sum=0;
		while(temp>0)
		{
			m=temp%10;
			fact=1;
			for(j=1;j<=m;++j)
			fact*=j;
			sum+=fact;
			temp=temp/10;
		}
		if(sum==n)
		sum1+=n;
	}
	printf("%d",sum1);
	return 0;
}
