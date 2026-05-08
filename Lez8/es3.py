lista1=[1,3,5,7]
lista2=[2,4,6]

lista=[x*i for i in lista1 for x in lista2 if x*i>10]
print(lista)