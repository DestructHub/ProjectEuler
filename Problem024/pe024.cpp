//code created by NamanNimmo Gera.
//12:48 pm, April 10, 2019.

#include<bits/stdc++.h>
using namespace std;

int main(){
    string x = "0123456789";
    for(int i = 1;i<1e6;i++)next_permutation(x.begin(),x.end());
    cout<<x;
    return 0;
}
