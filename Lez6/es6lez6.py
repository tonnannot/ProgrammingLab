while True:
    try:
        n = int(input("Inserisci un numero intero: "))
        print("Quadrato:", n ** 2)
        break
    except ValueError:
        print("Errore: inserire un numero intero valido")