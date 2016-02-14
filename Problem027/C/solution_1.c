/*
 * =====================================================================================
 *
 *                      Copyright 2016 Manoel Vilela
 *
 *         Author: Manoel Vilela
 *        Contact: manoel_vilela@engineer.com
 *   Organization: UFPA
 *
 * =====================================================================================
**/

#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#define LIMIT 1000


typedef struct {
    int primes;
    int a;
    int b;
} Result;


int quadratic(int n, int a, int b) {
    return n*n + a*n + b; 
}

// simple function
// to check if is a prime
int isPrime(int n) {
    if (n < 2) {
        return false;
    }
    for (int q = 2; q < sqrt(n) + 1; q++) {
        if (n % q == 0) {
            return false;
        }
    }

    return true;
}

// func evaluation n² + an + b
// return the n primes generate without gaps
// between [0, n]
int evalFunc(int a, int b){
    int n = 0;
    while (true) {
        if (isPrime(quadratic(n, a, b))){
            n += 1;
        } else {
            break;
        }
    }
    return n;
}

// get the optimal a, b
// and the nPrimes for
// equation f(n) = n² + an + b
// whose  f(n) -> [0, N]
// and N is MAX for LIMIT
void getresult(Result *r) {
    r->a = 0; r->b = 0; r->primes=0;
    for (int i = -LIMIT; i < LIMIT; i++) {
        for (int j = -LIMIT; j < LIMIT; j++ ) {
            int n = evalFunc(i, j);
            if (n > r->primes) {
                r->a = i;
                r->b = j;
                r->primes = n;;
            }
        }
    }
    // save
    
}

int main(int argc, char *argv[]) {
    Result r;
    getresult(&r);
    printf("Equation: n² + %dn + %d\n", r.a, r.b);
    printf("Number of primes: [0, %d]\n", r.primes);
    printf("Answer: %d\n", r.a * r.b);
}
