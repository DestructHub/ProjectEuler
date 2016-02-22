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


/*

A solução para uma computação eficiente disso é saber como fatorar rapidamente uma
expressão do tipo A ^ B mod C = x
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation


*/

#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

char* slice(char *array, long long s, long long e) {
    char *array_sliced;
    array_sliced = malloc(sizeof(char) * (e - s));

    int index = 0;
    for (int i = s; i < e; i++) {
        array_sliced[index] = array[i];
        index++;
    }

    return array_sliced;
}

int main(int argc, char *argv[]) {
    long long num = 0;
    for (int i = 1; i <= 1000; i++){
        printf("%li\n", num);
        num += fmod(pow(i, i), 1e10);
    }

    sprintf(num, "%li", num);
    
    return 0;

}