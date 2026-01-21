# Rigorous Definition of What the Code Calculates

Let $P$ be the ordered set of prime numbers, where $p_i$ denotes the $i$-th prime ($p_1=2, p_2=3, \dots$).

### 1. The Primorial ($N_n$)
Let $N_n$ be the product of the first $n$ primes (the primorial $p_n\$), defined as:

$$
N_n = \prod_{i=1}^{n} p_i
$$

### 2. The Domain ($S_n$)
Let $S_n$ be the set of integers modulo $N_n$. This set corresponds to the ring $\mathbb{Z}/N_n\mathbb{Z}$ (often denoted as $\mathbb{Z}_{N_n}$), representing the residue classes:

$$
S_n = \mathbb{Z}/N_n\mathbb{Z} = \{ k \in \mathbb{Z} \mid 0 \leq k < N_n \}
$$

Note that the cardinality $|S_n| = N_n$.

### 3. The Subset of Divisible Numbers ($W_n$)
Let $W_n$ be the subset of $S_n$ containing elements divisible by at least one of the first $n$ primes. This is defined as:

$$
W_n = \{ k \in S_n \mid \exists i \in \{1, \dots, n\}, k \equiv 0 \pmod{p_i} \}
$$

### 4. The Ratio $E(n)$
The function $E(n)$ is defined as the measure of $W_n$ within the space $\mathbb{Z}/N_n\mathbb{Z}$:

$$
E(n) = \frac{|W_n|}{N_n} = \frac{|W_n|}{\prod_{i=1}^{n} p_i}
$$

This definition formalizes the idea of how many numbers have at least one of the first $n$ primes as a divisor. For example, $E(1) = 0.5$ and $E(2) \approx 0.66$.

### 5. Recursive Definition
An algebraic expression for $E(n)$ using the Inclusion-Exclusion Principle is the sum of reciprocals of the first $n$ primes, minus the sum of 2-products reciprocals, plus the sum of 3-products of reciprocals, and so on.

Refactoring this leads to the recursive relationship:

$$
E(n) = E(n-1)\left(1 - \frac{1}{p_n}\right) + \frac{1}{p_n}
$$

Or:

$$
E(n+1) = E(n)\left(1 - \frac{1}{p_{n+1}}\right) + \frac{1}{p_{n+1}}
$$

Where the base case is $E(1) = 1/2$.

### 6. The Complementary Function $Q(n)$
To simplify calculation and analyze asymptotic behavior, we define $Q(n)$ as the measure of the complement set (numbers in $S_n$ that are *not* divisible by any of the first $n$ primes).

$$
Q(n) = 1 - E(n)
$$

Substituting $E(n) = 1 - Q(n)$ into the recursive formula:

$$
1 - Q(n) = [1 - Q(n-1)]\left(1 - \frac{1}{p_n}\right) + \frac{1}{p_n}
$$

Expanding the right side:

$$
1 - Q(n) = \left(1 - \frac{1}{p_n}\right) - Q(n-1)\left(1 - \frac{1}{p_n}\right) + \frac{1}{p_n}
$$

Simplifying the constant terms ($1 - \frac{1}{p_n} + \frac{1}{p_n} = 1$):

$$
1 - Q(n) = 1 - Q(n-1)\left(1 - \frac{1}{p_n}\right)
$$

This reduces to a purely multiplicative recursion for $Q(n)$:

$$
Q(n) = Q(n-1)\left(1 - \frac{1}{p_n}\right)
$$

Unrolling this recursion yields the **Euler Product Formula** for the density of coprimes:

$$
Q(n) = \prod_{i=1}^{n} \left(1 - \frac{1}{p_i}\right)
$$

Consequently, $E(n)$ can be calculated non-recursively as:

$$
E(n) = 1 - \prod_{i=1}^{n} \left(1 - \frac{1}{p_i}\right)
$$

This form allows for the application of Mertens' Third Theorem for high-speed estimation at large $n$:

$$
\lim_{n \to \infty} Q(n) \approx \frac{e^{-\gamma}}{\ln(p_n)}
$$

$$
\lim_{n \to \infty} E(n) \approx 1- \frac{e^{-\gamma}}{\ln(p_n)}
$$

Using this approach, we have found that $E(80,000,000) \approx 0.973517$. This confirms that as $n \to \infty$, $Q(n) \to 0$ and $E(n) \to 1$.
