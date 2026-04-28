class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
        try:
            with open(self.name,'r') as file:
                contenuto=file.readline()
        except Exception:
            raise ExamException("file nn aperto")
        if not contenuto:
            raise ExamException("file vuoto")
    
    def get_data(self):
        lista=[]
        file=open(self.name,'r')
        for line in file:
            line=line.strip().split(',')
            if line[0] != 'date':
                anno=line[0]
                try:
                    temp=int(line[1])
                    if temp <=0:
                        continue
                except Exception(ValueError,IndexError):
                    raise ExamException("non int")
                lista.append([anno,temp])
        return lista
    
def compute_variations(time_series, first_year, last_year):
    
    d={}
    for element in time_series:
        anno=int(element[0].split('-')[0])
        if first_year <=anno<=last_year:
            if anno not in d:
                d[anno]=[]
            d[anno].append(int(element[1]))
    
    d1={}
    anni=sorted(d.keys())
    
    for k in d.keys():
        media=sum(d[k])/len(d[k])
        d[k]=media
    
    for i in range(1, len(anni)):
        chiave=f"{anni[i-1]}-{anni[i]}"
        valore=d[anni[i]]-d[anni[i-1]]
        d1[chiave]=valore
    return d1

time_series_file=CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
print(time_series)

print("\n\n\n\n\n")
c=compute_variations(time_series, 1953, 1955)
print(c)