class ExamException(Exception):
    pass

class CSVTimeSeriesFile:
    def __init__(self,name):
        self.name=name
        try:
            with open(self.name,'r') as file:
                file.readline()
        except Exception:
            raise ExamException("file non aperto")
            
    def get_data(self):
        lista=[]
        file=open(self.name,'r')
        for line in file:
            line=line.strip().split(',')
            if line[0] != 'dt':
                anno=line[0]
                try:
                    temp=float(line[1])
                    if temp <=0:
                        continue
                except(ValueError,IndexError):
                    raise ExamException("non float o non ci sono abbastanza colonne")
                    continue
                lista.append([anno,temp])
                
        return lista
        
def compute_variations(time_series, first_year, last_year, N):
    lunghezza_finestra=last_year-first_year+1
    if N>=lunghezza_finestra:
        raise ExamException("n minore")
    d={}
    for element in time_series:
        anno=int(element[0].split('-')[0])
        if first_year <= anno <= last_year:
            if anno not in d:
                d[anno]=[]
            d[anno].append(float(element[1]))
            
    d1={}
    anni=sorted(d.keys())
    for k in d.keys():
        media=sum(d[k])/len(d[k])
        d[k]=media
    
    
    for i in range(N, len(anni)):
        anni_precedenti=anni[i-N:i]
        media_mobile=sum([d[a] for a in anni_precedenti])/N
    
        valore=d[anni[i]]-media_mobile
        d1[str(anni[i])]=valore
        
        
    return d1
    
    
time_series_file = CSVTimeSeriesFile(name='GlobalTemperatures.csv')
time_series = time_series_file.get_data()
print(time_series)


print("\n\n\n\n\n")
c=compute_variations(time_series, 1902, 1905, 1)
print(c)