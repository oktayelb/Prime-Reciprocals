# 📊 Prime-Reciprocals

A compact C program that dives into an elegant mathematical sequence involving **prime reciprocals**—and how they relate to which numbers are divisible by primes.

---

## 🧮 The Core Idea

We define a sequence recursively like this:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}E_{n+1}=E_n\left(1-\frac{1}{p_{n+1}}\right)+\frac{1}{p_{n+1}}" alt="Recursive Formula">
</p>

It starts with:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}E_0=\frac{1}{2}" alt="Initial Value">
</p>

Here, \( p_{n+1} \) is the \((n+1)\)th prime number.

---

## 🧠 What's Actually Going On?

This sequence, \( E_n \), represents the **proportion of natural numbers** that are divisible by **at least one** of the first \(n\) prime numbers.

There’s also a closed-form expression for it:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}E_n=1-\prod_{i=1}^n\left(1-\frac{1}{p_i}\right)" alt="Closed Form">
</p>

This formula comes from the **inclusion–exclusion principle**—it’s a clever way to count how many numbers are divisible by any among a group of divisors.

---

## ✨ Why This Is Interesting

While playing around with this, I noticed that as you include more and more primes, the value of \( E_n \) gets closer and closer to 1:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}\lim_{n\to\infty}E_n=1" alt="Limit">
</p>

This matches the intuition that **almost every natural number is divisible by at least one prime**—after all, only 1 isn’t!

---

## 🚀 Performance Tweaks

Originally, computing the sequence for large \( n \) was slow. I sped things up by using **dynamic programming** to cache intermediate results. That alone gave a **100× speedup**. It now runs smoothly even for large values of \( n \).

---

## 🔬 Bonus Explorations

I couldn’t resist going deeper—so I tried some fun variations:

- **Using squared primes** instead of primes:
  
  <p align="center">
    <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}B_n=1-\prod_{i=1}^n\left(1-\frac{1}{p_i^2}\right)\approx1-\frac{6}{\pi^2}\approx0.39207" alt="Bn Series">
  </p>

  This relates to the Riemann zeta function!

- **Combining multiple primes**: exploring numbers divisible by products of 2 or 3 distinct primes using more advanced inclusion–exclusion.

More of these ideas might find their way into the repo soon.

---

## 📦 What’s In the Repo?

- `prime_reciprocal.c`: main C file with the recursive logic  
- `README.md`: this file 😊

---

## 🧩 Coming Soon

Some planned additions:

- A full breakdown of how the recursive formula is derived  
- Generalizations to squared primes, prime triples, etc.  
- Plots and visualizations to show how fast these series converge  

---

## ✅ In a Nutshell

- Beautiful recursive structure  
- Grounded in number theory  
- Efficient and optimized  
- Converges to meaningful constants  

---

Thanks for checking this out! If you’re into prime numbers, recursion, or just enjoy seeing math and code come together, you’ll probably enjoy tinkering with this project too.
