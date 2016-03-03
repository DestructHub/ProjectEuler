/**
 * Find the sum of all even fibonacci numbers whose values are  under 4E6.
 */

#include <iostream>
#include <cstdlib>

int main(int argc, char *argv[])
{
    const char *argv_number = "4000000";

    if (argv[1]) {
	argv_number = argv[1];
    }
    
    // sum of all even fibonacci numbers.
    int sum = 0;
    
    int i = 0;
    int limit_number = atoi(argv_number);
    int last_fib = 1;
    int fib_number = 2;
    int fib_tmp = 0;
    
    while (fib_number < limit_number) {
	if (fib_number % 2 == 0) {
	    sum += fib_number;
	}
	
	fib_tmp = fib_number;
	fib_number += last_fib;
	last_fib = fib_tmp;
	i++;
    }
    
    std::cout << sum << std::endl;
    
    return 0;
}
