#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 8. Escriu una funció que elimini tots els espais d'una cadena.

def eliminar_espais(cadena):
    return cadena.replace(" ", "")

frase_amb_espais = input("Introdueix una frase amb espais: ")
frase_sense_espais = eliminar_espais(frase_amb_espais)
print("La frase sense espais és:", frase_sense_espais)