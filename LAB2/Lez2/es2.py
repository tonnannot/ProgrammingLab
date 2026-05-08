import numpy as np


a = np.arange(1, 21).reshape(5, 4)


b = a[[1, 3]]  
c = a[[2]]      

print(a / c)    