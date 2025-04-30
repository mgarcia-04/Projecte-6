#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 13. Escriu una funció que sumi tots els nombres d'una llista.

def sumar_llista(llista):
    suma = sum(llista)
    return suma

numeros = [1, 2, 3, 4, 5]
total = sumar_llista(numeros)
print("La suma dels nombres de la llista és:", total)