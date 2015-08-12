/**
 * C++ algorithm to get the sum of all prime numbers between a range of 2 and the number desired. 
 */
 
#include <iostream>
#include <cstdlib>
 
bool is_prime(unsigned int number);
 
int main(int argc, char* argv[])
{
	if(!argv[1])
	{
		std::cout << "Usage: primes <number_of_primes>" << std::endl;
	}
	else
	{
		std::cout << "You've choosen the sum of the first " << argv[1] 
		          << " prime numbers." << std::endl;
		
		// iteration variables.
		int i = 1;
		int j = 0;
		// the number to reach.
		int number_to = atoi(argv[1]);
 
		int sum = 0;
 
		while(j < number_to)
		{
			if(is_prime(i))
			{
				std::cout << i << std::endl;		
				sum += i;
				j++;
			}
			i++;
		}
 
		std::cout << "The sum of the numbers between 2 and " << number_to  
				  << " are: " << sum << std::endl;
	}
}
 
bool is_prime(unsigned int number) 
{ 
	if (number <= 1) 
		return false;
 
    unsigned int i;
    for (i=2; i*i<=number; i++) 
	{
        if (number % i == 0) 
		{
			return false;
		}
    }
    return true;
}