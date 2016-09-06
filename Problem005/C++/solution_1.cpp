#include <iostream>

int main(int argc, char **argv)
{
	int number = 2520;

	// naive solution
	while (true) {
		for (int i = 2; i <= 20; i++) {
			if (number % i != 0) {
				break;
			}
			else if (i == 20 && number % i == 0) {
				std::cout << number << std::endl;
				return 0;
			}
		}
		number++;
	}

	return 0;
}
