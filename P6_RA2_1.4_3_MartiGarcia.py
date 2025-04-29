#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Taula multiplicar

try:
  num_str = input("Introdueix un nombre enter per veure la seva taula de multiplicar: ")
  num = int(num_str)
  print(f"\nTaula de multiplicar del {num}:\n")
  for i in range(1, 11):
    resultat = num * i
    print(f"{num} x {i} = {resultat}")

except ValueError:
  print("Error: Si us plau, introdueix un nombre enter vàlid.")