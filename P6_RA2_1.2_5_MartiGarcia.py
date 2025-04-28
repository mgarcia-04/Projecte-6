#Cicle: ASIX
#Autor: Martí Garcia
#Data: 25-04-25
#Versio: 1.0
#Descripcio: Edat segons any actual

from datetime import date

data_naixement = int(input("Introdueix la data de naixement: "))
data_actual = date.today().year

edat = data_actual - data_naixement

print (f"La teva edat és de {edat} anys")

if edat >= 18:
    print ("És major d'edat!")
else:
    print ("És menor d'edat!")