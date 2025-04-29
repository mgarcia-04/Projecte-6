#Cicle: ASIX
 #Autor: Martí Garcia
 #Data: 29-04-25
 #Versio: 1.0
 #Descripcio: Numero primer o no

def es_primer(num):
  if num <= 1:
    return False
  if num <= 3:
    return True
  if num % 2 == 0 or num % 3 == 0:
    return False
  i = 5
  while i * i <= num:
    if num % i == 0 or num % (i + 2) == 0:
      return False
    i += 6
  return True

try:
  numero = int(input("Introdueix un número enter positiu: "))
  if numero <= 0:
    print("Si us plau, introdueix un número enter positiu.")
  else:
    if es_primer(numero):
      print(f"{numero} és un nombre primer.")
    else:
      print(f"{numero} no és un nombre primer.")
      
except ValueError:
  print("Si us plau, introdueix un número enter vàlid.")