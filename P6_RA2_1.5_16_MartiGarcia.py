#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 16. Fes un programa que elimini els duplicats d'una llista.

nombres_amb_duplicats = [1, 2, 2, 3, 4, 4, 5]
nombres_sense_duplicats = list(set(nombres_amb_duplicats))
print("La llista sense duplicats és:", nombres_sense_duplicats)