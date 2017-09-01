/*
 * =============================================================================
 *
 *                      Copyright 2016 Manoel Vilela
 *
 *         Author: Manoel Vilela
 *        Contact: manoel_vilela@engineer.com
 *   Organization: UFPA
 *
 * =============================================================================
**/


/*

A solução para uma computação eficiente disso é saber como fatorar rapidamente
uma expressão do tipo: A ^ B mod C = x

=> (A_1 * A_2 * A_3 ... A_B) mod C                 (exponentiation definition)
=> ((A_1 mod C) * (A_2 mod C) * ... (A_B mod C))   (distributive mod property)
=> (A mod C) ^ B                                   (exponentiation definition)

*/

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>
#include <stdint.h>


uint64_t pow_mod(uint64_t x, uint64_t e, uint64_t mod) {
    uint64_t result = 1;
    x %= mod;
    while(e--) {
        result = (result % mod) * x;
    }

    return result;
}

int main(void) {
    uint64_t num = 0;
    uint64_t mod = (uint64_t) 1E10;
    for (uint64_t i = 1; i <= 1000; i++){
        num = (num + pow_mod(i, i, mod)) % mod;
    }

    printf("%lu\n", num);
    return 0;
}
