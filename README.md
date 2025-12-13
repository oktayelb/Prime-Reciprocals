### Rigorous Definition of $E(n)$

Let $P$ be the ordered set of prime numbers, where $p_i$ denotes the $i$-th prime ($p_1=2, p_2=3, \dots$).

**1. The Primorial ($N_n$)**
Let $N_n$ be the product of the first $n$ primes (the primorial $p_n\$), defined as:
$$N_n = \prod_{i=1}^{n} p_i$$

**2. The Domain ($S_n$)**
Let $S_n$ be the set of integers modulo $N_n$. This set corresponds to the ring $\mathbb{Z}/N_n\mathbb{Z}$ (often denoted as $\mathbb{Z}_{N_n}$), representing the residue classes:
$$S_n = \mathbb{Z}/N_n\mathbb{Z} = \{ k \in \mathbb{Z} \mid 0 \leq k < N_n \}$$
Note that the cardinality $|S_n| = N_n$.

**3. The Subset of Divisible Numbers ($W_n$)**
Let $W_n$ be the subset of $S_n$ containing elements divisible by at least one of the first $n$ primes. This is defined as:
$$W_n = \{ k \in S_n \mid \exists i \in \{1, \dots, n\}, k \equiv 0 \pmod{p_i} \}$$

**4. The Ratio $E(n)$**
The function $E(n)$ is defined as the measure of $W_n$ within the space $\mathbb{Z}/N_n\mathbb{Z}$:
$$E(n) = \frac{|W_n|}{N_n} = \frac{|W_n|}{\prod_{i=1}^{n} p_i}$$

---

That definition formalizes the idea of how many numbers have at least one of the first $n$ primes as a divisor. 

$E(1)$ gives us 0.5 and $E(2)$ gives us 0.66

An algebraic expression for $E(n)$ would be the sum of reciprocals of the first $n$ primes, minus the sum of 2-products reciprocals, plus the sum of 3-products of reciprocals, all the way up to $n$.

Refactoring this gives:

$$
E(n) = E(n-1)\left(1 - \frac{1}{p_n}\right) + \frac{1}{p_n}
$$

Or:

$$
E(n+1) = E(n)\left(1 - \frac{1}{p_{n+1}}\right) + \frac{1}{p_{n+1}}
$$

Where $E(1) = 1/2$. Using this approach, and implementing dynamic programming solutions, I have found that $E(80,000,000) \approx 0.973517$.
