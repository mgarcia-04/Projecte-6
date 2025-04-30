#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 6. Demana una cadena i mostra la primera i l'última lletra.

cadena = input("Introdueix una cadena: ")
if cadena:
    primera_lletra = cadena[0]
    ultima_lletra = cadena[-1]
    print("La primera lletra és:", primera_lletra)
    print("L'última lletra és:", ultima_lletra)
else:
    print("La cadena està buida.")