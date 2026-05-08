class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        data = []
        try:
            with open(self.name, "r") as f:
                for i, line in enumerate(f):
                    if i == 0:
                        continue  # salta header
                    line = line.strip()
                    if not line:
                        continue
                    data.append(line.split(","))
        except FileNotFoundError:
            print(f"Errore: file '{self.name}' non trovato")
            return None
        return data


class NumericalCSVFile(CSVFile):
    def get_data(self):
        data = super().get_data()
        if data is None:
            return None

        numerical_data = []

        for row in data:
            try:
                # prima colonna resta stringa (data)
                new_row = [row[0]]
                # converte le altre colonne a float
                for value in row[1:]:
                    new_row.append(float(value))
                numerical_data.append(new_row)
            except ValueError as e:
                print(f"Errore nella riga {row}: {e}")
                # salta la riga

        return numerical_data


# Test
file = NumericalCSVFile("shampoo_sales.csv")
print(file.get_data())
#commit