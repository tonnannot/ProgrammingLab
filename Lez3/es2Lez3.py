# 1
def conta_parole(lista):
    d = {}
    for p in lista:
        d[p] = d.get(p, 0) + 1
    return d


# 2
def somma_shampoo(file_name):
    totale = 0.0
    with open(file_name, "r") as f:
        next(f)  # salta header
        for line in f:
            parts = line.strip().split(",")
            try:
                totale += float(parts[1])
            except:
                continue
    return totale


# 3
def conta_parola(file_name, parola):
    count = 0
    with open(file_name, "r") as f:
        for line in f:
            count += line.split().count(parola)
    return count


# 4
def conteggio(file_name):
    d = {}
    with open(file_name, "r") as f:
        for line in f:
            for w in line.split():
                d[w] = d.get(w, 0) + 1
    return d


# 5
def rimuovi_duplicati(file_name):
    visti = set()
    with open(file_name, "r") as f:
        righe = f.readlines()

    with open("unique.txt", "w") as f:
        for r in righe:
            if r not in visti:
                f.write(r)
                visti.add(r)

print(conta_parole(["ciao", "ciao", "test"]))  # {'ciao': 2, 'test': 1}