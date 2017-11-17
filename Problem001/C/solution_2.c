/*
 * Implementation of solution 1 using Principle of inclusion-exclusion
 * The proof is done on the related pull request.
 * by Luiz Peres
 * Obs.: I'm using a lot of variables in order to make it easy to understand
 */

#include <stdio.h>
#define LAST_N 999

int main()
{
  int div3       = LAST_N / 3;
  int div5       = LAST_N / 5;
  int div3Union5 = LAST_N / (3*5);
  int sumMult3   = 3 * div3 * (div3 + 1) / 2;
  int sumMult5   = 5 * div5 * (div5 + 1) / 2;
  int sumMult3Union5 = 3 * 5 * div3Union5 * (div3Union5 + 1) / 2;

  int inc_exc = sumMult3 + sumMult5 - sumMult3Union5;
  printf("%d\n", inc_exc);

  return 0;
}
