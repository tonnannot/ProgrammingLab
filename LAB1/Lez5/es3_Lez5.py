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

    # Punto 1: verifica se insegna tutti i corsi dello studente
    def insegna_tutti(self, studente):
        return all(corso in self.corsi for corso in studente.corsi)


# Punto 2: verifica che esistano docenti per tutti i corsi dello studente
def verifica_docenti_per_studente(studente, docenti):
    for corso in studente.corsi:
        if not any(corso in docente.corsi for docente in docenti):
            return False
    return True


# Test
corsi_studente = ["Programmazione", "Analisi", "Geometria"]

studente = Studente("Irene", "Rossi", corsi_studente)

doc1 = Docente("Mario", "Bianchi", ["Programmazione", "Analisi"])
doc2 = Docente("Luisa", "Verdi", ["Geometria", "Fisica"])

docenti = [doc1, doc2]

# Punto 1
print(doc1.insegna_tutti(studente))  # False
print(doc2.insegna_tutti(studente))  # False

# Punto 2
print(verifica_docenti_per_studente(studente, docenti))  # True
#commit