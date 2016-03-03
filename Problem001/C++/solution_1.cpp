/*
 * Find the sum of all multiples of 3 and 5 below 1000 
 */

#include <iostream>
#include <cstdlib>

int main(int argc, char* argv[])
{
    // upper default limit.
    const char *limit = "1000";
    
    if (argv[1]) {
	limit = argv[1];
    }
    
    // iterator variable.
    int i = 0;
    // resultant sum of all multiples of 3 and 5.
    int sum = 0;
    // transform an array of characters into an integer.
    int number_to = atoi(limit);
	
    while (i < number_to) {
	if ((i % 3 == 0) && (i % 15 != 0)) {
	    sum += i;
	}
 	if ((i % 5 == 0)) {
	    sum += i;
	}
	i++;
    }
    
    std::cout << sum << std::endl;

    return 0;
}
