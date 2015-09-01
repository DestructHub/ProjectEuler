/*
 * =====================================================================================
 *
 *                      Copyright 2015 Manoel Vilela
 *
 *
 *       Filename: solution_1.c 
 *
 *    Description: Solution for Problem001 of projecteuler
 *
 *         Author: Manoel Vilela
 *        Contact: manoel_vilela@engineer.com
 *   Organization: UFPA
 *
 * =====================================================================================
**/



/*
Multiples of 3 and 5
Problem 1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
*/


#include <stdio.h>
#include <stdlib.h>
#define MAX 1000

/*===================================================
 *
 *      Author: That's it's a very old solution 
 *      when i've beginning with programming in C.
 *
 * ==================================================
**/

// ?
int sumlista(int* lista, int lenght){
	int sum = 0;
	for(int i = 0; i < lenght; i++){
		sum += lista[i];;
	}
	return sum;
}

// why so much pointers for this?
void increase(int **data, int *lenght){
	int size = *lenght + sizeof(int);
	*data = (int*) realloc(*data, size * sizeof(int));
	*lenght += 1;
}

//it's really stupid
int exist(int *lista, int lenght, int num){
	int exist = 0;
	for(int i = 0; i <= lenght; i++)
		if (lista[i] == num)
			exist = 1;
	return exist;
}

// i really doubt my skill for simplify after see my past
int main(void){
	int *lista, lenght = 0;
	int multiples[3] = {3, 5, 0};
	lista = (int*) malloc(sizeof(int));
	
	for(int i = 0; i < MAX; i++){
		for (int j = 0; multiples[j] != 0; j++){
			int mult = multiples[j];
			if (i % mult == 0){
				if (!exist(lista, lenght, i)){
					printf("Multiply %d: %d\n", mult, i);
					lista[lenght] = i;
					increase(&lista, &lenght);
				}
			}
		}
	}
	
	int sum = sumlista(lista, lenght);
	
    //at least works... right?
    printf("Sum: %d\n", sum);
	free(lista);

	return 0;
}