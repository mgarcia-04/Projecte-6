#Cicle: ASIX
#Autor: Martí Garcia
#Data: 28-04-25
#Versio: 1.0
#Descripcio: Numero aleatori

import random

numero_aleatori = random.randint(1, 100)

print ("He pensat un numero entre 1 i 100, intenta endevinarlo")

while True:
    numero_usuari_str = input("Quin número creus que és? ")
    numero_usuari = int(numero_usuari_str)

    if numero_usuari > numero_aleatori:
        print ("El número és més petit")
    elif numero_usuari < numero_aleatori:
        print ("El número és més gran")
    else:
        print (f"Felicitats! L'has encertat!")
        break