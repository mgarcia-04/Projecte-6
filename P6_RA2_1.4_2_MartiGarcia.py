#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Llista numeros

try:
  num_str = input("Introdueix un nombre enter positiu: ")
  num = int(num_str)
  if num <= 0:
    print("Error: Si us plau, introdueix un nombre enter positiu.")
  else:
    suma_total = sum(range(1, num + 1))
    print(f"La suma dels nombres des de 1 fins a {num} és: {suma_total}")
    
except ValueError:
  print("Error: Si us plau, introdueix un nombre enter vàlid.")