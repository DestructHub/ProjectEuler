/**
 * C++ algorithm to get the sum of all prime numbers between a range of 2 and the number desired. 
 */

#include <iostream>
#include <cstdlib>

bool is_prime(unsigned int number);
 
int main(int argc, char* argv[])
{
    const char *num = "2000000";
    
    if (argv[1]) {
	num = argv[1];
    }
    
    // iteration variables.
    int i = 1;
    // the number to reach.
    int number_to = std::atoi(num);
    
    long long int sum = 0;
    
    while (i < number_to) {
	if (is_prime(i)) {
	    std::cerr << i << std::endl;		
	    sum += i;
	}
	i++;
    }
    
    std::cout << sum << std::endl;
}
 
bool is_prime(unsigned int number) 
{ 
  if (number <= 1) { 
      return false;
  }
 
  unsigned int i;
  for (i=2; i*i<=number; i++) {
      if (number % i == 0) {
	  return false;
      }
  }

  // naive solution
  /*for (i = 2; i < 10; i++) {
      if (number % i == 0)
	  return false;
  }*/
  
  return true;
}
