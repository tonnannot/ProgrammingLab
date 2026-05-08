lst_inpt=[i for i in range(1,21)]

lst = [(a,b,c) for a in lst_inpt for b in lst_inpt for c in lst_inpt if a**2 + b**2 == c**2]

print(lst)