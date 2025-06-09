try:
    with open("nombres.txt", "r", encoding="utf-8") as fitxer:
        for linia_num, linia in enumerate(fitxer, start=1):
            linia = linia.strip()
            try:
                num = int(linia)
                print(f"Línia {linia_num}: {num}")
            except ValueError:
                print(f"Error: la línia {linia_num} no és un enter vàlid ('{linia}')")
except FileNotFoundError:
    print("Error: 'nombres.txt' no existeix.")
