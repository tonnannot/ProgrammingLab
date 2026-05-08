# 1
def somma_lista(lista):
    return sum(lista)


# 2
def is_palindromo(s):
    return s == s[::-1]


# 3
def scambia(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A


# 4
def hanno_elemento_in_comune(lista1, lista2):
    return any(elem in lista2 for elem in lista1)


# 5
def numeri_in_italiano(lista):
    mapping = ["zero","uno","due","tre","quattro","cinque","sei","sette","otto","nove"]
    return [mapping[n] for n in lista]


# Test
print(somma_lista([1,2,3]))                         # 6
print(is_palindromo("anna"))                        # True
print(scambia([1,2,3], 0, 2))                       # [3,2,1]
print(hanno_elemento_in_comune([1,2,3], [3,4,5]))   # True
print(numeri_in_italiano([1,0,7,9,8]))              # ["uno","zero","sette","nove","otto"]
#commit