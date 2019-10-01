#include<bits/stdc++.h>
using namespace std;

const int much = 1000000;
bool isPrime [much];

void sieve (){
	memset (isPrime, true, sizeof(isPrime));
	isPrime[0] = isPrime [1] = false;
	for (int i = 2; i < much; ++i)
		for (int j = (i << 1); j < much; j += i)
			isPrime [j] = false;
}

bool test (int t)
{
	int orig = t, cnt = 0, tmp10 = 1;
	while (t > 0){
		if (!isPrime [t])
			return false;
		t /= 10;
		++cnt, tmp10 *= 10;
	}
	while (orig > 0)
	{
		if (!isPrime[orig])
			return false;
		orig = (orig % (tmp10 /= 10));
	}
	return true;
}

int main ()
{
	long long sum = 0;
	sieve ();
	for (int i = 10; i < much; ++i)
		if (test(i))
			sum += i;
	cout << sum << '\n';
	return 0;
}
