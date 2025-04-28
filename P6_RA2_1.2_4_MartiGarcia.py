#Cicle: ASIX
#Autor: Martí Garcia
#Data: 25-04-25
#Versio: 1.0
#Descripcio: Aprovat o suspés

num_str = input("Introdueix la teva nota: ")
num = float(num_str)

if num >= 5:
    print("Has aprovat")
else:
    print("Has suspés")