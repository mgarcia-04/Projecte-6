#Cicle: ASIX
#Autor: Martí Garcia
#Data: 25-04-25
#Versio: 1.0
#Descripcio: Vocal o Consonant

lletra = input("Introdueix una lletra: ").lower()

if len(lletra) == 1 and lletra.isalpha():
    vocals = "aeiou"
    if lletra in vocals:
       print(f"La lletra '{lletra}' és una vocal.")
    else:
       print(f"La lletra '{lletra}' és una consonant")