#include<bits/stdc++.h>
using namespace std;

int main(){
  char numbers[] = "0123456789";
  for(int i=1;i<1000000;i++)
    next_permutation(numbers,numbers+10); 
  cout << numbers << endl;
}
