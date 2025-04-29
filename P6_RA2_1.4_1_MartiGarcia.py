#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Llista numeros

try:
  limit_str = input("Introdueix un nombre enter per al límit de la seqüència: ")
  limit = int(limit_str)
  for i in range(limit + 1):
    print(i)
except ValueError:
  print("Error: Si us plau, introdueix un nombre enter vàlid.")