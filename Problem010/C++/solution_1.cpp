/**  Copyright @ Rafael C. Nunes | Lol, my cpplint requires that suck message on header!
 * C++ algorithm to get the sum of all prime numbers between a range of 2 and the number desired. 
 */

#include <iostream>
#include <cstdlib>
#include <string.h>

bool is_prime(unsigned int number);

int main(int argc, char* argv[]) {
    const char *num = "2000000";

    if (strcmp(argv[1], "--help") == 0) {
        std::cerr << "Usage: primes <number_of_primes>" << std::endl;
        exit(0);
    } else if (argv[1]) {
        num = argv[1];
    }

    // iteration variables.
    int i = 1;
    int j = 0;
    // the number to reach.
    int number_to = atoi(num);

    int sum = 0;

    while (j < number_to) {
        if (is_prime(i)) {
            sum += i;
            j++;
        }
        i++;
    }

    std::cout << sum << std::endl;
}

bool is_prime(unsigned int number) {
    if (number <= 1)
        return false;

    unsigned int i;
    for (i = 2; i * i <= number; i++) {
        if (number % i == 0) {
            return false;
        }
    }
    return true;
}
