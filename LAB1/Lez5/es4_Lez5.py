class Poligono:
    def __init__(self, numero_lati):
        self.numero_lati = numero_lati

    def descrizione(self):
        return f"Sono un poligono con {self.numero_lati} lati"


class Quadrilatero(Poligono):
    def __init__(self):
        super().__init__(4)

    def descrizione(self):
        return "Sono un quadrilatero"


class Rettangolo(Quadrilatero):
    def __init__(self, base, altezza):
        super().__init__()
        self.base = base
        self.altezza = altezza

    def descrizione(self):
        return f"Sono un rettangolo con base {self.base} e altezza {self.altezza}"

    def perimetro(self):
        return 2 * (self.base + self.altezza)

    def area(self):
        return self.base * self.altezza


class Triangolo(Poligono):
    def __init__(self, lato1, lato2, lato3):
        super().__init__(3)
        self.lato1 = lato1
        self.lato2 = lato2
        self.lato3 = lato3

    def descrizione(self):
        return f"Sono un triangolo con lati {self.lato1}, {self.lato2}, {self.lato3}"

    def perimetro(self):
        return self.lato1 + self.lato2 + self.lato3

    def is_equilatero(self):
        return self.lato1 == self.lato2 == self.lato3


# Test
p = Poligono(5)
q = Quadrilatero()
r = Rettangolo(4, 6)
t = Triangolo(3, 3, 3)

print(p.descrizione())
print(q.descrizione())
print(r.descrizione(), "| Perimetro:", r.perimetro(), "| Area:", r.area())
print(t.descrizione(), "| Perimetro:", t.perimetro(), "| Equilatero:", t.is_equilatero())