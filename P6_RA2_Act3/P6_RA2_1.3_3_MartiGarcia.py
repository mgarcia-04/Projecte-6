nova_linia = "Aquesta és una nova línia afegida.\n"

with open("sortida.txt", "a", encoding="utf-8") as fitxer:
    fitxer.write(nova_linia)
