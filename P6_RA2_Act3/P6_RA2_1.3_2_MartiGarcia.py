linies = [
    "Aquesta és la primera línia.\n",
    "Aquesta és la segona línia.\n",
    "Aquesta és la tercera línia.\n"
]

with open("sortida.txt", "w", encoding="utf-8") as fitxer:
    fitxer.writelines(linies)
