/*
 * Find the difference between the square of the sum and the sum of the squares
 * of the first one hundred numbers.
 *
 * Square sum:
 *
 * (1+2+3+...+98+99+100)^2 = 5050^2 (Thanks Gauss)
 *
 * Sum square:
 *
 * 1^2+2^2+3^2+...+98^2+99^2+100^2
 */

#include <iostream>
#include <cmath>

long int sum_of_squares();

int main(int argc, char **argv)
{
	// From math: Sum of n natural numbers is: [n*(n+1)]/2;
	long int square_sum = pow(((100*(100+1))/2), 2);

	std::cout << square_sum - sum_of_squares() << std::endl;

	return 0;
}

/*
 * Naive sum of the squares.
 */
long int sum_of_squares()
{
	long int acc = 0;

	for (int i = 1; i <= 100; i++) {
		acc += pow(i, 2);
	}

	return acc;
}
