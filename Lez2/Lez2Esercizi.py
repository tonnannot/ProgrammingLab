# 1
def minuti_a_ore(minuti):
    h = minuti // 60
    m = minuti % 60
    print(f"{h}h:{m}min")


# 2
n = int(input("Numero: "))
print("Quadrato:", n**2)
print("Cubo:", n**3)


# 3
n = int(input("Numero: "))
print("Pari" if n % 2 == 0 else "Dispari")


# 4
def conta_lettera(parola, lettera):
    return parola.count(lettera)


# 5
n = int(input("Numero: "))
if n < 2:
    print("Non primo")
else:
    primo = True
    for i in range(2, n):
        if n % i == 0:
            primo = False
            break
    print("Primo" if primo else "Non primo")


# 6
somma = 0
while True:
    n = int(input("Numero (0 per uscire): "))
    if n == 0:
        break
    somma += n
print("Somma:", somma)


# 7
def fattoriale(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f


# 8
def tipo_triangolo(a, b, c):
    if a + b <= c or a + c <= b or b + c <= a:
        return "Non è un triangolo"
    if a == b == c:
        return "Equilatero"
    elif a == b or a == c or b == c:
        return "Isoscele"
    else:
        return "Scaleno"


# 9
def conta_vocali(s):
    vocali = "aeiouAEIOU"
    return sum(1 for c in s if c in vocali)


# Test rapidi
print(conta_lettera("ciao", "a"))
print(fattoriale(5))
print(tipo_triangolo(3,3,3))
print(conta_vocali("programmazione"))   