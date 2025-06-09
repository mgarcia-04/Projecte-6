try:
    with open("resultats.txt", "w", encoding="utf-8") as fitxer:
        fitxer.write("Intentem escriure en aquest fitxer.\n")
except PermissionError:
    print("Error: No tens permisos per escriure al fitxer 'resultats.txt'.")
