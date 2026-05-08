from datetime import datetime

def calcola_eta_e_prossimo_compleanno(data_nascita_str):
    # formato atteso: YYYY-MM-DD
    nascita = datetime.strptime(data_nascita_str, "%Y-%m-%d")
    oggi = datetime.now()

    # età
    eta = oggi.year - nascita.year
    if (oggi.month, oggi.day) < (nascita.month, nascita.day):
        eta -= 1

    # prossimo compleanno
    prossimo = datetime(oggi.year, nascita.month, nascita.day)
    if prossimo < oggi:
        prossimo = datetime(oggi.year + 1, nascita.month, nascita.day)

    delta = prossimo - oggi

    giorni = delta.days
    secondi_tot = delta.seconds

    ore = secondi_tot // 3600
    minuti = (secondi_tot % 3600) // 60
    secondi = secondi_tot % 60

    print(f"Età: {eta} anni")
    print(f"Tempo al prossimo compleanno: {giorni} giorni, {ore} ore, {minuti} minuti, {secondi} secondi")


# Test
data = input("Inserisci data di nascita (YYYY-MM-DD): ")
calcola_eta_e_prossimo_compleanno(data)
#commit