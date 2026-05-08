
import numpy as np

# 1a) Quadrati
squares_loop = []
for x in range(6):
    squares_loop.append(x ** 2)

squares_lc = [x ** 2 for x in range(6)]

# 1b) Filtro pari
evens_loop = []
for x in range(10):
    if x % 2 == 0:
        evens_loop.append(x)

evens_lc = [x for x in range(10) if x % 2 == 0]

# 1c) Uppercase di stringhe
words = ['hello', 'world', 'python']
upper_loop = []
for w in words:
    upper_loop.append(w.upper())

upper_lc = [w.upper() for w in words]

print(squares_lc)  
print(evens_lc) 
print(upper_lc)     