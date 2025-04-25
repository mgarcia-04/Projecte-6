num1 = float(input("Introdueix el primer número: "))
num2 = float(input("Introdueix el segon número: "))
operacio = input("Introdueix l'operació (+, -, *, /): ")

if operacio == '+':
  resultat = num1 + num2
  print("El resultat de la suma és:", resultat)
elif operacio == '-':
  resultat = num1 - num2
  print("El resultat de la resta és:", resultat)
elif operacio == '*':
  resultat = num1 * num2
  print("El resultat de la multiplicació és:", resultat)
elif operacio == '/':
  if num2 != 0:
    resultat = num1 / num2
    print("El resultat de la divisió és:", resultat)
  else:
    print("Error! No es pot dividir per zero.")
else:
  print("Operació no vàlida. Si us plau, introdueix +, -, *, o /.")