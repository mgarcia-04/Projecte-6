#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 9. Crea un programa que divideixi una frase en paraules i les mostri una per una.

frase = input("Introdueix una frase: ")
paraules = frase.split()
print("Les paraules de la frase són:")
for paraula in paraules:
    print(paraula)