#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Frase vocals

def contar_vocals(frase):
  vocals = "aeiouAEIOU"
  comptador = 0
  for lletra in frase:
    if lletra in vocals:
      comptador += 1
  return comptador

frase_usuari = input("Introdueix una frase: ")
num_vocals = contar_vocals(frase_usuari)
print(f"La frase conté {num_vocals} vocals.")