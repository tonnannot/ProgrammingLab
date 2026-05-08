while True:
    print("\nMENU")
    print("1. Somma di due numeri")
    print("2. Differenza tra due numeri")
    print("3. Uscita")

    scelta = input("Scegli un'opzione (1-3): ")

    if scelta == "1":
        try:
            a = float(input("Primo numero: "))
            b = float(input("Secondo numero: "))
            print("Risultato:", a + b)
        except ValueError:
            print("Errore: inserire numeri validi")

    elif scelta == "2":
        try:
            a = float(input("Primo numero: "))
            b = float(input("Secondo numero: "))
            print("Risultato:", a - b)
        except ValueError:
            print("Errore: inserire numeri validi")

    elif scelta == "3":
        print("Uscita dal programma")
        break

    else:
        print("Errore: opzione non valida")