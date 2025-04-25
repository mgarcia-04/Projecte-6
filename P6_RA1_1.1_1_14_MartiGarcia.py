preu_sense_iva = float(input("Introdueix el preu del producte sense IVA: "))
iva = 0.21
preu_amb_iva = preu_sense_iva * (1 + iva)
print("El preu amb un IVA del 21% és:", preu_amb_iva)