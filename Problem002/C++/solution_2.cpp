#include<bits/stdc++.h>
using namespace std;
bool odd(int i){
   return i & 1;
}
int main(){
   vector<int> fib(30);
   fib[0] = 1;
   adjacent_difference (fib.begin(), fib.end()-1,fib.begin()+1,
                  std :: plus<int>());   
   fib.erase (std :: remove_if (fib.begin(), fib.end(), odd),
                     fib.end());
   //clock_t end(clock() - start);
   std :: cout << accumulate (fib.begin(), fib.end(),
                     0);
   return 0;
}
