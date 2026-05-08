
nested = [[1, 2, 3], [4, 5], [6, 7, 8, 1]]

flat = [x for sublist in nested for x in sublist]

print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 1]
#commit