def estat_persona(edat):
    if edat < 18:
        return "Menor d'edat", "Encara ets jove"
    elif edat < 65:
        return "Adult", "Edat laboral i activa"
    else:
        return "Jubilat", "Temps per gaudir de la jubilació"

for edat in [12, 25, 70]:
    estat, descripcio = estat_persona(edat)
    print(f"Edat: {edat} → Estat: {estat} - {descripcio}")