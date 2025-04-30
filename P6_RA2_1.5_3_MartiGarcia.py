#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 3. Escriu una funció que reverteixi una cadena.

def invertir_cadena(cadena):
    return cadena[::-1]

paraula = input("Introdueix una paraula: ")
invertida = invertir_cadena(paraula)
print("La cadena invertida és:", invertida)