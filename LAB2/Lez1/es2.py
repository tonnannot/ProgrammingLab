import numpy as np

# 2.1 — Scritto direttamente
primes = np.array([2, 3, 5, 7])

# 2.2 — Lunghezza con len() e .size
print(len(primes))   
print(primes.size)   

# 2.3 — dtype: interi → int64
print(primes.dtype)   # int64

# 2.4 — Con list comprehension + funzione is_prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes_lc = np.array([n for n in range(11) if is_prime(n)])
print(primes_lc)  