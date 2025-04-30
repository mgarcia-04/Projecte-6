#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 12. Demana a l'usuari 5 paraules i emmagatzema-les en una llista.

paraules = []
for i in range(5):
    paraula = input(f"Introdueix la paraula {i+1}: ")
    paraules.append(paraula)
print("La llista de paraules és:", paraules)