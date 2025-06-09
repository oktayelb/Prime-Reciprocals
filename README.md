# 📊 Prime-Reciprocals

A compact C program that explores a fascinating mathematical series involving the **reciprocals of prime numbers** and their relation to the **divisibility of natural numbers**.

---

## 🧮 Formula

The sequence is defined recursively:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}E_{n+1}=E_n\left(1-\frac{1}{p_{n+1}}\right)+\frac{1}{p_{n+1}}" alt="Recursive Formula">
</p>

With initial value:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}E_0=\frac{1}{2}" alt="Initial Value">
</p>

Here,  p{n+1} is the (n+1) th prime number.

---

## 🧠 Interpretation

This sequence captures the **proportion of natural numbers** divisible by **at least one** of the first \(n\) primes.

In closed form:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}E_n=1-\prod_{i=1}^n\left(1-\frac{1}{p_i}\right)" alt="Closed Form">
</p>

This is derived using the **inclusion–exclusion principle**, treating each prime as a “divisor event.”

---

## ✨ Motivation

While experimenting with prime reciprocals, I suspected that this sequence would converge to:

<p align="center">
  <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}\lim_{n\to\infty}E_n=1" alt="Limit">
</p>

Intuitively, this means that **almost all natural numbers** are divisible by at least one prime as the set of primes grows.

---

## 🔁 Optimizations

The original implementation was slow for large \(n\), so I introduced **dynamic programming** to cache partial results. This reduced computation time by over **100×**.

---

## 🔬 Related Explorations

This project inspired further generalizations:

- Using **squares of primes**:

  <p align="center">
    <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\color{White}B_n=1-\prod_{i=1}^n\left(1-\frac{1}{p_i^2}\right)\approx1-\frac{6}{\pi^2}\approx0.39207" alt="Bn Series">
  </p>

- Using **products of 2 or 3 distinct primes**, forming inclusion–exclusion over those combinations.

More of these variants may be added to the repo later!

---

## 📦 Summary

✅ Elegant recursive structure  
✅ Strong number-theoretic foundation  
✅ Optimized with dynamic programming  
✅ Converges to beautiful constants

---

## 📁 File Overview

- `prime_reciprocal.c`: core C implementation of the recursive formula  
- `README.md`: you're reading it 😊

---

## 🧩 Coming Soon

I plan to include:

- The full derivation of the recursive formula  
- Generalizations for squared primes and multi-prime products  
- Charts and visualizations of convergence behavior

Stay tuned!
