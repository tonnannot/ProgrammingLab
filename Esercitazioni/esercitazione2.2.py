class ExamException(Exception):
    pass

class CSVTimeSeriesFile:

    def __init__(self,name):
        self.name=name
        
    def get_data(self):
        lista=[]
        file=open(self.name, 'r')
        for line in file:
            line=line.strip().split(',')
            if line[0] != 'date':
                data=line[0]
                passeggeri=line[1]
                lista.append([data, passeggeri])
            
        return lista

def compute_variations(time_series, first_year, last_year):
    d={}
    for element in time_series:
        anno=int(element[0].split('-')[0])
        if first_year <= anno <= last_year:
            if anno not in d.keys():
                d[anno]=[]
            d[anno].append(int(element[1]))

    for k in d.keys():
        media=sum(d[k])/len(d[k])
        d[k]=media
    
    d_1={}

    anni=sorted(d.keys())
    for i in range(1, len(anni)):
        chiave=f"{anni[i-1]}-{anni[i]}"
        valore=d[anni[i]]-d[anni[i-1]]
        d_1[chiave]=valore
    return d_1

time_series_file = CSVTimeSeriesFile(name='data.csv')
time_series = time_series_file.get_data()
c=compute_variations(time_series, 1949, 1951)
print(c)