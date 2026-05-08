lista_a = [0, 1, 3, 4]
lista_b = ['a', 'b', 'c']

result = [(x, y) for x in lista_a for i, y in enumerate(lista_b) if x % 2 == 0 if i % 2 != 0]

print(result)  # [(0, 'b'), (4, 'b')]
#commit