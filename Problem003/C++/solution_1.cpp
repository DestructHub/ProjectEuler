#include<bits/stdc++.h>
using namespace std;

long long int largestPrime(long long int num){
  int j=2;
  while(num%j != 0) j+=1;
  if(num%2 == 0){
    if(num==2) return 2;
    else return largestPrime(num/2);
  }
  else if(num/j == 1) return num;
  else return largestPrime(num/j);
}

int main(){
  long long int x=600851475143;
  cout<<((long long int)largestPrime(x))<<endl;
}
