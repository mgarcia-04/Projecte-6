with open("sortida.txt", "r+", encoding="utf-8") as fitxer:
    contingut = fitxer.read()
    print("Contingut actual:")
    print(contingut)

    fitxer.write("Línia afegida al final amb mode r+.\n")
