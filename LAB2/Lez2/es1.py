import numpy as np


primes = np.array([2, 3, 5, 7, 11, 13, 17, 19])

# Maggiori di 10
print(primes[primes > 10])        

# Numeri primi pari (solo il 2)
print(primes[primes % 2 == 0])      

# Maschera booleana > 10
print(primes > 10)  
