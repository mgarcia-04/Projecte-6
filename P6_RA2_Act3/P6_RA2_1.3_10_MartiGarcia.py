fitxer = None
try:
    fitxer = open("alguna_dada.txt", "r", encoding="utf-8")
    for linia in fitxer:
        if "ERROR" in linia:
            raise RuntimeError("S'ha trobat un error dins del fitxer")
        print(linia.strip())
except FileNotFoundError:
    print("El fitxer no existeix.")
except RuntimeError as e:
    print(f"Error durant la lectura: {e}")
finally:
    if fitxer:
        fitxer.close()
        print("Fitxer tancat correctament.")
