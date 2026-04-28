class Canguro:
    def __init__(self, contenuto_tasca=None):
        if contenuto_tasca is None:
            self.contenuto_tasca = []
        else:
            self.contenuto_tasca = contenuto_tasca

    def intasca(self, oggetto):
        self.contenuto_tasca.append(oggetto)

    def __str__(self):
        return f"Canguro con tasca: {self.contenuto_tasca}"


# Test
can = Canguro()
guro = Canguro()

can.intasca("mela")
can.intasca(42)

print("can:", can)
print("guro:", guro)