class CSVFile:
    def __init__(self, name):
        self.name = name
        try:
            with open(self.name, "r") as f:
                f.readline()  # verifica esistenza file
        except FileNotFoundError:
            print(f"Errore: il file '{self.name}' non esiste")

    def get_data(self):
        data = []
        try:
            with open(self.name, "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    data.append(line.split(","))
        except FileNotFoundError:
            print(f"Errore: impossibile aprire il file '{self.name}'")
            return None

        return data


# Test
csv = CSVFile("data.csv")
print(csv.get_data())
