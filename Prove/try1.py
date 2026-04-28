# variabili

temperatura = 8.5
anno = 1900
nome = "Italia"

# if

if temperatura > 0:
    print("positiva")
elif temperatura == 0:
    print ("zero")
else: 
    print("negativa")


# for
valori = [8.5, 9.2, 7.1, 10.3]

for v in valori:
    print(v)

# operazioni dentro al for

totale = 0
for v in valori:
    totale = totale + v

media = totale / len(valori)
print(media) # 8.775

# funzioni

def calcola_media(lista):
    totale = 0
    for v in lista:
        totale = totale + v
    return totale / len(lista)

# uso:
risultato=calcola_media([8.5, 9.2, 7.1])
print(risultato) #8.266....



temperatura = 9

if temperatura>0:
    print("pos")
elif temperatura==0:
    print("zero")
else:
    print("neg")

temperatura=-5

if temperatura>0:
    print("pos")
elif temperatura ==0:
    print("z")
else:
    print("neg")

vals = [5, 7, 8, 10]

for v in vals:
    print(v)

tot=0

for v in vals:
    tot=tot+v

med=tot/len(vals)
print(med)

def somma_positivi(lista):
    tota=0
    for v in lista:
        if v>0:
            tota=tota+v
    return tota

riss=somma_positivi([5, -3, 10, 2, -6])
print(riss)


print("\n \n parte 2\n")
# liste

valori = [8.5, 9.2, 7.1]

valori.append(10.3)
print(len(valori))
print(valori[0])
print(valori[-1])

# dizionari

d = {}
d["1900"] = [8.5, 9.2, 7.1]
d["1901"] = [8.8, 9.0]

print(d["1900"])
print(d["1901"])

if "1900" in d:
    print("esiste")

for chiave in d:
    print(chiave, d[chiave])


# pattern fondamentale esame

dati = [
    ["1900-01", 8.5],
    ["1900-02", 9.2],
    ["1901-01", 8.8],
    ["1901-03", 9.0],
]

per_anno={}

for riga in dati:
    anno = riga[0][:4] # prende i primi 4 caratteri: "1900"
    valore = riga[1]

    if anno not in per_anno:
        per_anno[anno] = [] # crea lista vuota per quell'anno

    per_anno[anno].append(valore) #aggiunge valore

print(per_anno)
# {"1900": [8.5, 9.2], "1901": [8.8, 9.0]}


# es 2

dati = [
    ["1900-01", 8.5],
    ["1900-06", 9.2],
    ["1900-11", 7.8],
    ["1901-02", 8.8],
    ["1901-07", 9.1],
]

per_anno={}

for riga in dati:
    anno=riga[0][:4]
    valore=riga[1]

    totale=0
    if anno not in per_anno:
        per_anno[anno]= []
    
    per_anno[anno].append(valore)
    medie={}
    for anno in per_anno:
        valori=per_anno[anno]
        medie[anno]=sum(valori)/len(valori)


print(medie)


# es 3

per_anno={}

for riga in dati:
    anno=riga[0][:4]
    valore=riga[1]

    if anno not in per_anno:
        per_anno[anno]= []

    per_anno[anno].append(valore)


medie={}
for anno in per_anno:
    valori=per_anno[anno]
    valori_filtrati=[]
    for v in valori:
        if v > 8.0:
            valori_filtrati.append(v)

    medie[anno]=sum(valori_filtrati)/len(valori_filtrati)
        
print("medie filtrate: ",medie)

print("\n \n LE CLASSI \n")
# elemento centrale esame: LE CLASSI

class Termometro:

    def __init__(self, nome):
        self.nome = nome
        self.misurazioni = []

    def aggiungi(self, valore):
        self.misurazioni.append(valore)

    def media(self):
        if len(self.misurazioni) == 0:
            return 0
        return sum(self.misurazioni) / len(self.misurazioni)
    
t1 = Termometro(nome="Roma")
t2 = Termometro(nome="Milano")

t1.aggiungi(8.5)
t1.aggiungi(9.2)
t2.aggiungi(7.1)

print(t1.media()) # 8.85
print(t2.media()) # 7.1


print("\n \n esercizio 4: classe calcolatrice \n")

# es 4

class Calcolatrice:

    def __init__(self, valore_iniziale):
        self.valore = valore_iniziale

    def aggiungi(self, n):
        self.valore = n + self.valore
    
    def risultato(self):

        return self.valore

c = Calcolatrice(valore_iniziale=10)

c.aggiungi(5)
c.aggiungi(3)
print(c.risultato()) # 18


print("\n \n tipo struttura esame \n")

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name        # salva il nome del file

    def get_data(self):
        # 1. Apri il file
        try:
            f = open(self.name, 'r')
        except Exception:
            raise Exception("Errore: impossibile aprire il file.")
        
        result = []

        with f:
            for line in f:
                line = line.strip() #rimuove \n e spazi

                if not line: #salta righe vuote
                    continue

                fields = line.split(',') # divide per virgla -> lista

                if len(fields) < 2: #riga malformata
                    continue

                data = fields[0]
                valore_str = fields[1]

                #2. converti il valore in float, salta se non funziona
                try:
                    valore = float(valore_str)
                except ValueError:
                    continue

                #3. salta valori non validi
                if valore <=0:
                    continue

                result.append([data, valore])
        return result


print("\n \n Esercizio 5: classe CSVTimeSeriesFile \n")

# es 5

class CSVTimeSeriesFile:

    def __init__(self, name):
        self.name = name
    
    def get_data(self):
        try:
            f = open(self.name, 'r')
        except Exception:
            raise Exception("Errore: impossibile aprire il file.")
        
        result = []

        with f: 
            for line in f:
                line = line.strip()

                if not line:
                    continue

                fields = line.split(',')

                if len(fields) < 2:
                   continue
                data_str = fields[0]
                valore_str=fields[1]

                try:
                    valore =float(valore_str)
                except ValueError:
                    continue
            
                if valore <0:
                    continue

                result.append([data_str, valore])
        return result
    