#Casagrande Tommaso, SM32A00052

class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self, name):
        self.name=name
        #(1) controllo esistenza file; primo caso validazioni
        try:
            with open(self.name,'r') as file:
                lettura=file.readline()
        except Exception:
            raise ExamException("Errore: il file non è stato aperto: inesistente")
        if not lettura:
            raise ExamException("Errore: file vuoto")
    
    def get_data(self):
        #creo lista vuota a cui verranno assegnate le coppie di [anno, consumo]
        lista=[]
        file=open(self.name,'r')
    
        #scorriamo ogni linea (righe) del file per recuperare i valori
        for line in file:
            #puliamo spazi e \n con strip() e dividiamo 0 e 1 con la ,
            line=line.strip().split(",")
            #saltiamo l'intestazione
            if line[0] != 'date':
                #primo elemento stringa
                data=str(line[0])
            #secondo elemento float
            try:
                consumo=float(line[1])
            
            #(2) ignoro i valori non numeri(grazie a continue), 
            # come richiesto dal secondo caso delle validazioni
            except ValueError:
                continue
        #assegniamo alla nostra lista le varie coppie di valori una per una
            lista.append([data, consumo])
        return lista



def compute_annual_mean(time_series, first_year, last_year):
    
    if not isinstance(first_year, int) or not isinstance(last_year, int):
        raise ExamException("Errore: first_year e last_year devono essere interi.")

    #creo dizionario che riempiremo con chiavi (anni) e valori (medie) 
    d={}
    #scorriamo ogni elemento nella nostra time_series definita da get_data():
    #   time_series=time_series_file.get_data() nel main
    for element in time_series:
        #(3) passo gli anni in formato int (intero) da str (stringa), 
        # che avevo passato nella get_data() in tale formato
        # terzo caso delle validazioni
        
        #recuperiamo l'anno dai nostri elementi 1 a 1, dividendo mese 
        #ed anno per / e prendendo il valore [1], che è l'anno (saltando il mese)
        anno=int(element[0].split('/')[1])

        #print(anno)
        #print(element[0])
        #print(element[1])
        
        #controllo che sia nel nostro intervallo
        if first_year <= anno <= last_year:
            #se non è nel dizionario, lo riempiamo con chiavi e valori
            if anno not in d:
                #assegnamo le chiavi al diz, con anno, ed ad ognuna
                #una lista vuota 
                d[anno]=[]
            #infine assegnamo il valore di ogni mese per ognuno degli anni, 1 ad 1
            d[anno].append(float(element[1]))
        
    #creiamo un dizionario nuovo per riempirlo con quello richiesto
    #dall'esercizio, ovvero le medie
    d_1={}
    #riordiniamo le chiavi degli anni dentro all'intervallo 
    #e ogni chiave la assegnamo a questa nuova lista "anni"
    anni=sorted(d.keys())

    #per ogni anno, in ordine, calcola media e al valore della chiave
    #assegna la media
    for k in d.keys():
        media=sum(d[k])/len(d[k])
        d[k]=media
    
    #ultimo ciclo, partendo da 0 fino a un range che è la lunghezza della
    #lista che avevamo creato "anni", creiamo 1 ad 1 chiave e valore
    #da poter assegnare al nostro nuovo dizionario d_1, sfruttando
    #la lista "anni" che avevamo creato
    for i in range(0, len(anni)):
        chiave=f"{anni[i]}"
        valore=d[anni[i]]
        valore=round(valore, ndigits=2)

        d_1[chiave]=valore
    
    #ritorno finale, dizionario d_1 con anni e medie corrette.
    return d_1

time_series_file = CSVTimeSeriesFile(name="electricity.csv")
time_series = time_series_file.get_data()
#print(time_series)

c=compute_annual_mean(time_series, 2019, 2021)
#d=compute_annual_mean(time_series, 2018, 2018)
print(c)
#print(d)
print("c")