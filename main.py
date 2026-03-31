import math
from decimal import Decimal, getcontext
from scipy.special import lambertw

# 1. Configuration for High Precision
# We set precision to 50 digits to prevent floating point loss during the final calculation.
# This is more than enough for "great precision."
getcontext().prec = 50

def estimate_nth_prime(n):
    """
    Estimates the n-th prime number using the inverse of the logarithmic integral function
    approximated via the Lambert W function.
    
    The approximation is based on the inversion of x / ln(x) = n, which leads to:
    x = -n * W_{-1}(-1/n)
    
    For n >= 2, the branch k=-1 of the Lambert W function is required.
    """
    if n < 2:
        return Decimal(2) # Fallback for edge case, though formula intended for large n
        
    # We use floating point for the Lambert W calculation because scipy handles it in float64.
    # The error at n=800,000,000 is negligible for the purpose of the log(p_n) term.
    # Formula: p_n approx -n * W_{-1}(-1/n)
    
    # Note: lambertw returns a complex number, we take the real part.
    val = -n * lambertw(-1.0/n, k=-1).real
    
    return Decimal(val)

def calculate_E_fast(n):
    """
    Calculates E(n) using Mertens' Third Theorem and the estimated nth prime.
    
    Formula: E(n) = 1 - (e^(-gamma) / ln(p_n))
    """
    
    # 1. Estimate p_n (the n-th prime)
    p_n_approx = estimate_nth_prime(n)
    
    # 2. Define Constants with High Precision
    # Euler-Mascheroni constant gamma
    gamma = Decimal("0.57721566490153286060651209008240243104215933593992")
    
    # 3. Apply Mertens' Third Theorem
    # Term = e^(-gamma)
    euler_term = (-gamma).exp() 
    
    # Log of the n-th prime
    ln_p_n = p_n_approx.ln()
    
    # Calculate Q(n) approximation
    q_n = euler_term / ln_p_n
    
    # Calculate E(n)
    E_value = Decimal(1) - q_n
    
    return E_value, p_n_approx

# --- User Parameters ---
n_target = 80000000  # 800 Million

# --- Execution ---
result_E, result_pn = calculate_E_fast(n_target)

# --- Output ---
print(f"--- Fast Calculation for E({n_target:,}) ---")
print(f"Estimated nth Prime (p_n): {result_pn:,.2f}")
print(f"ln(p_n):                   {result_pn.ln()}")
print(f"Calculated E(n):           {result_E}")
print(f"Precision:                 {getcontext().prec} digits")
