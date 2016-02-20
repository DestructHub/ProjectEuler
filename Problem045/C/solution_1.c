/*
 * ===========================================================
 *
 *                      Copyleft 2016 Manoel Vilela
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
#include <math.h>
#define BModule 1

typedef struct {
	double a;
	double c;
} Polynom;

int main(int argc, char *argv[]) {
	Polynom P = {3, 2};
	Polynom H = {2, 1};

	double last_triangle = 285;

	while (1) {
		last_triangle += 1;
		double t = (pow(last_triangle, 2) + last_triangle) / 2;
		double Pn = (BModule + sqrt(BModule + 4 * P.a * P.c * t)) / (2 * P.a);	
 		double Hn = (BModule + sqrt(BModule + 4 * H.a * H.c * t)) / (2 * H.a);	

		if (floor(Pn) == Pn && floor(Hn) == Hn) {
			printf("%.0f\n", t);
			break;
		}
	}
	return 0;
}
