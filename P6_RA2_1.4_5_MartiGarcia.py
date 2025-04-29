#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Numeros primers

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
  limit_str = input("Introdueix un nombre enter positiu: ")
  limit = int(limit_str)
  if limit < 2:
    print("No hi ha nombres primers en aquest rang (són majors o iguals a 2).")
  else:
    print(f"Nombres primers des de 2 fins a {limit}:")
    for num in range(2, limit + 1):
      if es_primer(num):
        print(num, end=" ")

except ValueError:
  print("Error: Si us plau, introdueix un nombre enter vàlid.")