#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 13. Escriu una funció que sumi tots els nombres d'una llista.

parells = []
senars = []
for i in range(10):
    try:
        numero = int(input(f"Introdueix el número {i+1}: "))
        if numero % 2 == 0:
            parells.append(numero)
        else:
            senars.append(numero)
    except ValueError:
        print("Si us plau, introdueix un nombre enter vàlid.")

print("La llista de nombres parells és:", parells)
print("La llista de nombres senars és:", senars)