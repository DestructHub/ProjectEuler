#include<stdio.h>
long long int g[1001][1001];
int main() 
{ 
	long long int i=1,m=500,n=500,sum=0,j;
	g[m][n++]=i++;
	while(i<=1002001)
	{
		g[m++][n]=i++;
		while(m<n)
		{
			g[m++][n]=i++;
		}
		g[m][n--]=i++;
		while(m+n > 1000)
		{
			g[m][n]=i++;
			--n;
		}
		g[m--][n]=i++;
		while(m>n)
		{
			g[m][n]=i++;
			--m;
		}
		g[m][n++]=i++;
		while(m+n < 1000)
		{
			g[m][n]=i++;
			++n;
		}
		g[m][n++]=i++;
	}
	for(i=0;i<1001;++i)
	{
		for(j=0;j<1001;++j)
		{
			if(j==i || j+i==1000)
			sum=sum+g[i][j];
		}
	}
	printf("%lld",sum);
	return 0;
}
