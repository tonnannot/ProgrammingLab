class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno
        self.speed = 0

    def __str__(self):
        return f"{self.marca} {self.modello} ({self.anno}) - Velocità: {self.speed}"

    def accellerare(self):
        self.speed += 5

    def frenare(self):
        self.speed -= 5
        if self.speed < 0:
            self.speed = 0

    def get_speed(self):
        return self.speed
    #commit