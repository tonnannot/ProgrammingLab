class ExamException(Exception):
    pass

class MovingAverage:

    def __init__(self,lunghezza_finestra):
        self.lunghezza_finestra = lunghezza_finestra
    
    
    def compute(self, lista):
        listaa=[]
        for i in range(len(lista)-self.lunghezza_finestra+1):
            somma = sum(lista[i:i+self.lunghezza_finestra])
            media=somma/self.lunghezza_finestra
            listaa.append(media)
        return listaa
    
moving_average=MovingAverage(2)
result = moving_average.compute([2, 4, 8, 16])
print(result)

                        