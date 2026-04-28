class ExamException(Exception):
    pass


class CSVTimeSeriesFile:
    """Classe per leggere una time series da un file CSV."""

    def __init__(self, name):
        # Salva il nome del file
        self.name = name

    def get_data(self):
        """Legge il file CSV e ritorna una lista di liste [data, passeggeri]."""

        # Controlla che il file sia apribile
        try:
            file = open(self.name, 'r')
        except Exception:
            raise ExamException(f'Errore: impossibile aprire il file "{self.name}"')

        result = []
        last_date = None  # Per controllare l'ordine e i duplicati

        with file:
            for line in file:
                line = line.strip()

                # Ignora righe vuote
                if not line:
                    continue

                # Divide la riga in campi
                fields = line.split(',')

                # Servono almeno 2 campi (data e passeggeri)
                if len(fields) < 2:
                    print(f'Attenzione: riga ignorata (troppo corta): "{line}"')
                    continue

                date = fields[0].strip()
                value_str = fields[1].strip()

                # Controlla che la data abbia il formato YYYY-MM
                parts = date.split('-')
                if len(parts) != 2:
                    print(f'Attenzione: riga ignorata (data non valida): "{line}"')
                    continue
                try:
                    year = int(parts[0])
                    month = int(parts[1])
                    if month < 1 or month > 12:
                        raise ValueError
                except ValueError:
                    print(f'Attenzione: riga ignorata (data non valida): "{line}"')
                    continue

                # Controlla che il valore dei passeggeri sia un intero positivo
                try:
                    passengers = int(value_str)
                    if passengers <= 0:
                        raise ValueError
                except ValueError:
                    print(f'Attenzione: riga ignorata (valore passeggeri non valido): "{line}"')
                    continue

                # Controlla ordine e duplicati sulla data
                if last_date is not None:
                    if date == last_date:
                        raise ExamException(f'Errore: timestamp duplicato trovato: "{date}"')
                    if date < last_date:
                        raise ExamException(f'Errore: timestamp fuori ordine: "{date}" dopo "{last_date}"')

                last_date = date
                result.append([date, passengers])

        return result


def compute_variations(time_series, first_year, last_year):
    """
    Calcola le variazioni del numero medio di passeggeri anno per anno
    nell'intervallo [first_year, last_year].
    Ritorna un dizionario {"YYYY-YYYY": variazione, ...}.
    """

    # Controllo che gli anni siano stringhe
    if not isinstance(first_year, str) or not isinstance(last_year, str):
        raise ExamException('Errore: first_year e last_year devono essere stringhe')

    # Controllo che la time series non sia vuota
    if not time_series:
        raise ExamException('Errore: la time series è vuota')

    # Raccoglie tutti gli anni presenti nei dati
    years_in_data = set()
    for entry in time_series:
        year = entry[0].split('-')[0]
        years_in_data.add(year)

    # Controlla che first_year e last_year siano presenti nei dati
    if first_year not in years_in_data:
        raise ExamException(f'Errore: first_year "{first_year}" non presente nei dati')
    if last_year not in years_in_data:
        raise ExamException(f'Errore: last_year "{last_year}" non presente nei dati')

    # Controlla che first_year <= last_year
    if first_year > last_year:
        raise ExamException(f'Errore: first_year "{first_year}" è successivo a last_year "{last_year}"')

    # Raggruppa i passeggeri per anno nell'intervallo
    year_data = {}
    for entry in time_series:
        year = entry[0].split('-')[0]
        if first_year <= year <= last_year:
            if year not in year_data:
                year_data[year] = []
            year_data[year].append(entry[1])

    # Calcola la media per ogni anno (ignora anni senza dati)
    year_avg = {}
    for year in sorted(year_data.keys()):
        values = year_data[year]
        if values:  # Solo se ci sono misurazioni
            year_avg[year] = sum(values) / len(values)

    # Serve almeno 2 anni con dati per calcolare variazioni
    sorted_years = sorted(year_avg.keys())
    if len(sorted_years) < 2:
        raise ExamException('Errore: non ci sono abbastanza anni con dati per calcolare le variazioni')

    # Calcola le variazioni tra anni consecutivi (con dati)
    result = {}
    for i in range(1, len(sorted_years)):
        prev_year = sorted_years[i - 1]
        curr_year = sorted_years[i]
        diff = round(year_avg[curr_year] - year_avg[prev_year], 10)
        # Arrotonda a intero se il risultato è già intero
        if diff == int(diff):
            diff = int(diff)
        key = f"{prev_year}-{curr_year}"
        result[key] = diff

    return result


# --- Test ---
if __name__ == '__main__':
    time_series_file = CSVTimeSeriesFile(name='data.csv')
    time_series = time_series_file.get_data()

    print("Prime 5 righe della time series:")
    for row in time_series[:5]:
        print(row)

    print("\nVariazioni 1949-1951:")
    variations = compute_variations(time_series, "1949", "1951")
    for k, v in variations.items():
        print(f"  {k}: {v}")