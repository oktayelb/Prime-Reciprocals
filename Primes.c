#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define GLOB 8000

double arr[GLOB];
int primes[GLOB];

int isPrime(int k)
{

	if (k % 3 == 0 && k != 3) // No need to check for two  since the numbers will already be odd
		return 0;

    int x = sqrt(k);

	for (int i = 5; i <= x; i = i + 6)
		if (k % i == 0 || k % (i + 2) == 0)
			return 0;

	return 1;
}


// function which gives nth prime
// if nth prime is not in the primes array
// simply get the prime before and  count up
int nThPrime(int n)
{
    int temp = primes[n];
    if(temp != 0) return temp;


	int i=primes[n-1]+2;

	while(!isPrime(i))
        i+=2;

	primes[n] = i;
	return i;
}


double e(int x)
{
    if(x<=0)
		return  0;
    if(x == 1)
		return  0.5;

    double reciprocal = (1.0/nThPrime(x));  // 1/p_n
    double temp = arr[x-1];                 // E_(n-1)
    arr[x] = (temp*(1-reciprocal)) + reciprocal;
    return arr[x];


}
int main()
{
    arr[0]    = 0;
    arr[1]    = 0.5;
    arr[2]    = 2/3;
    primes[1] = 2;
    primes[2] = 3;
    primes[3] = 5;

    for(int i = 1;  i<GLOB; i++){
	printf("%f\n",e(i));

    }
	return 0;
}
