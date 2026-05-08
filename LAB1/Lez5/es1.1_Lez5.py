class Persona:
    def __init__(self, nome, cognome, corsi):
        self.nome = nome
        self.cognome = cognome
        self.corsi = list(corsi)


class Studente(Persona):
    def saluta(self):
        print(f"Ciao, sono {self.nome} {self.cognome}.")
        print(f"Frequento: {', '.join(self.corsi)}")


class Docente(Persona):
    def saluta(self):
        print(f"Sono il docente {self.nome} {self.cognome}.")
        print(f"Insegno: {', '.join(self.corsi)}")


corsi = ["Programmazione", "Laboratorio", "Analisi", "Geometria"]

obj_Irene = Studente("Irene", "Rossi", corsi)
obj_Irene.saluta()        
#commit