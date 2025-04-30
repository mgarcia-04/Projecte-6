#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 4. Demana una paraula i verifica si és un palíndrom (ex: "anna", "civic", etc.).

def es_palindrom(paraula):
    paraula = paraula.lower()
    return paraula == paraula[::-1]

paraula = input("Introdueix una paraula: ")
if es_palindrom(paraula):
    print("La paraula és un palíndrom.")
else:
    print("La paraula no és un palíndrom.")