class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def __str__(self):
        return f"Veicolo: {self.marca} {self.modello}"


class Auto(Veicolo):
    def __init__(self, marca, modello, numero_porte):
        super().__init__(marca, modello)
        self.numero_porte = numero_porte

    def __str__(self):
        return f"Auto: {self.marca} {self.modello}, Porte: {self.numero_porte}"


class Moto(Veicolo):
    def __init__(self, marca, modello, tipo):
        super().__init__(marca, modello)
        self.tipo = tipo

    def __str__(self):
        return f"Moto: {self.marca} {self.modello}, Tipo: {self.tipo}"


# Test
a = Auto("Fiat", "Panda", 5)
m = Moto("Yamaha", "R1", "Sportiva")

print(a)
print(m)