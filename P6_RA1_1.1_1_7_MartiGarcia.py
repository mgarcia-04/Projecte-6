num1 = float(input("Introdueix un número: "))
num2 = float(input("Introdueix el segon número: "))

resta = num1 - num2
multiplicacio = num1 * num2

if num2 != 0:
    divisio = num1 / num2
else:
    divisio = "No es pot dividir per zero"

print("La resta és:", resta)
print("La multiplicacio és:", multiplicacio)
print("La divisio és:", divisio)