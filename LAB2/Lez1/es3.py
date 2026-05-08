import numpy as np

# Array a generato con arange (senza digitarlo)
a = np.arange(1, 6)      

# b: sottoarray (slice)
b = a[1:4]                

# c: reverse di a
c = a[::-1]            

# Divisione elemento per elemento
print(a / c)              

# ── Stessa cosa con una lista Python ──
a_list = list(range(1, 6))        
c_list = a_list[::-1]            

# Le liste NON supportano / direttamente → serve list comprehension
div_list = [x / y for x, y in zip(a_list, c_list)]
print(div_list)            # [0.2, 0.5, 1.0, 2.0, 5.0]