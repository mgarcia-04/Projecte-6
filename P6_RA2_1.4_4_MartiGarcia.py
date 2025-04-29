#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Numeros parells

try:
  num_str = input("Introdueix un nombre enter positiu: ")
  num = int(num_str)
  if num < 0:
    print("Error: Si us plau, introdueix un nombre enter no negatiu.")
  else:
    print(f"Nombres parells des de 0 fins a {num}:")
    for i in range(0, num + 1, 2):
      print(i, end=" ")
except ValueError:
  print("Error: Si us plau, introdueix un nombre enter vàlid.")