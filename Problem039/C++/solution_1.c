#include <stdio.h>
#define MAX 1000
 
int main() {
    int i, j, k, maxP;
    int ps[1001];

    for(i = 1; i <= MAX; i++) {
        for(j = i;j <= MAX; j++) {
            for(k = j; (k * k) < (i * i + j * j); k++);
            if((i * i + j * j) == (k * k) && (i + j + k) <= MAX) {
                ps[i+j+k]++;
            }
        }
    }

    for(i = 1; i <= MAX; i++) {    
        if(ps[maxP] < ps[i])
            maxP = i;
    }

    printf("%d\n",maxP);

    return 0;
}
