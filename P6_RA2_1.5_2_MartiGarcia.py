#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 2. Demana una frase i compta quantes vocals conté.

frase = input("Introdueix una frase: ")
vocals = "aeiouAEIOU"
comptador = 0
for lletra in frase:
    if lletra in vocals:
        comptador += 1
print("La frase conté", comptador, "vocals.")