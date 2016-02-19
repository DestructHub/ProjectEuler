/*
 * ===========================================================
 *
 *                      Copyright 2016 Manoel Vilela
 *
 *
 *       Filename: solution_1.c
 *
 *    Description: Solution of Problem045 of the ProjectEuler
 *
 *         Author: Manoel Vilela
 *        Contact: manoel_vilela@engineer.com
 *   Organization: UFPA
 *
 * ============================================================
**/

// created by Manoel Vilela

#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>
#define F_ISINTEGER(_float) (!fmod(_float, 1.0f))

typedef struct {
	int a;
	int b;
	int c;
} Polynom;


float quadratic(int a, int b, int c) {
	return (-b + sqrt(b*b-4*a*c)) / (2 * a);
}

int main(int argc, char *argv[]) {

	Polynom P = {3, -1, -2};
	Polynom H = {2, -1, -1};

	float last_triangle = 285;

	while (true) {
		last_triangle += 1;
		int t = (pow(last_triangle, 2) + last_triangle) / 2;
		float p = quadratic(P.a, P.b, t * P.c);
		float h = quadratic(H.a, H.b, t * H.c);

		if (F_ISINTEGER(p) && F_ISINTEGER(h)) {
			printf("%d\n", t);
			break;
		}
	}
}
