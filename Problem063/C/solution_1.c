#include <stdio.h>
#include <math.h>

int num_length (double n) {
    if (n < 10)
        return 1;
    else
        return 1 + num_length(n / 10);
}


int main(int argc, char **argv) {
    int a, n; 
    int ndigits = 0;
    for (a = 1; a < 10; a++) {
        for (n = 1; n < 22; n++) {
            if (num_length(pow(a,n)) == n) {
                ndigits += 1;
            } 
        }
    }

    printf("%d\n", ndigits);
    return 0;
}