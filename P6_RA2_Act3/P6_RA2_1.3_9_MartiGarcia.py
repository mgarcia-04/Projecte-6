try:
    with open("fitxer_creat.txt", "r", encoding="utf-8") as fitxer:
        contingut = fitxer.read()
        print("Fitxer llegit correctament.")
except FileNotFoundError:
    print("El fitxer no existia, es crearà un de nou...")
    with open("fitxer_creat.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write("Fitxer creat automàticament.\n")
