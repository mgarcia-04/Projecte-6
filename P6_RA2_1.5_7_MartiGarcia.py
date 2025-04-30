#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 7. Demana una cadena i compta quantes vegades apareix una lletra concreta.

cadena = input("Introdueix una cadena: ")
lletra = input("Introdueix la lletra que vols comptar: ")
comptador = cadena.count(lletra)
print("La lletra", lletra, "apareix", comptador, "vegades a la cadena.")