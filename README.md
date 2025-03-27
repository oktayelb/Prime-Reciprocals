# Prime-Reciprocals
A really simple C code that calculates a mathemathical formula involving primes


![Formula](https://latex.codecogs.com/png.image?\dpi{200}\color{White}E_{n+1}=E_n\left(1-\frac{1}{p_{n+1}}\right)+\frac{1}{p_{n+1}})

Where 


![Formula](https://latex.codecogs.com/png.image?\dpi{200}\color{White}E_{0}=\frac{1}{2})



The nᵗʰ term shows how many natural numbers are divisible by at least one of the first n primes.

I had found a formula involving the reciprocals of primes, tied to the divisors of natural numbers.

My initial guess was that the sequence would converge to 1, and wrote the code to empirically see it. 

I will share the way I deduced this recursive definition

I used dynamic programming to  speed up the computations, which ended up speeding the process by  more than 100 fold.


