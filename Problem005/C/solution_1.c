#include <stdio.h>
// Author: tkovs
// Used lua solution that uses python solution XD

int main(void) {
    int k, i = 1, j;

    for (k = 1; k <= 20; k++) {
        if (i % k > 0) {
            for (j = 1; j <= 20; j++) {
                if ((i * j) % k == 0) {
                    i = i * j;
                    break;
                }
            }
        }
    }

    printf ("%d", i);

    return 0;
}