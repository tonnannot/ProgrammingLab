class CSVFile:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Il nome del file deve essere una stringa")
        self.name = name

    def get_data(self, start=1, end=None):
        if not isinstance(start, int) or start < 1:
            start = 1

        data = []

        try:
            with open(self.name, "r") as f:
                lines = f.readlines()
        except FileNotFoundError:
            print(f"Errore: file '{self.name}' non trovato")
            return None

        if end is None or end > len(lines):
            end = len(lines)

        # start/end sono 1-based e inclusivi
        for i in range(start - 1, end):
            line = lines[i].strip()
            if not line:
                continue
            data.append(line.split(","))

        return data


# Test
csv = CSVFile("shampoo_sales.csv")
print(csv.get_data(start=1, end=5))