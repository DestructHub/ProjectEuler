/*
 * Finds the 10001 prime number.
 */

#include <iostream>
#include <cstdlib>

bool is_prime(int n);

int main(int argc, char **argv)
{
	int n = 0;
	int prime_count = 1;

	int limit = 10001;

	if (argc > 1) {
		limit = std::atoi(argv[1]);
	}

	while (prime_count <= limit) {
		if (is_prime(n)) {
			++prime_count;
		}

		n++;
	}


	std::cout << n-1 << std::endl;

	return 0;
}

bool is_prime(int n)
{
	if (n < 2) {
		return false;
	}
	else if (n == 2 || n == 3) {
		return true;
	}
	else if (n % 2 == 0) {
		return false;
	}
	else  {
		for (int i = 2; i*i <= n; i++) {
			if (n % i == 0) {
				return false;
			}
		}
	}

	return true;
}
