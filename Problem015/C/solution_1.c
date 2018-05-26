#include<stdio.h>
unsigned long long g[21][21];
int main() 
{ 
    int j,i;
    for ( i = 0; i < 21; ++i) {
        g[i][0] = 1;
        g[0][i] = 1;
    }
    for (i = 1; i < 21; ++i) {
        for (j = 1; j < 21; ++j) {
            g[i][j] = g[i-1][j] + g[i][j-1];
        }
    }
    printf("%lld\n", g[20][20]);
    return 0;
}
