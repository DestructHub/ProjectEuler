#include <stdio.h>
int main()
{
	int i,j,a[100][100],k;
	for(i=0;i<100;++i)
	{
		for(j=0;j<=i;++j)
		scanf("%d",&a[i][j]);
	}
	for(i=99;i>0;--i)
	{
		for(j=0;j<i;++j)
		{
			if(a[i][j]>a[i][j+1]){
			  a[i-1][j]+=a[i][j];
      }
			else{
        a[i-1][j]+=a[i][j+1];
      }
		}
	}
	printf("%d",a[0][0]);
	return 0;
}
