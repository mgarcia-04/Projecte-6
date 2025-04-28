#Cicle: ASIX
#Autor: Martí Garcia
#Data: 25-04-25
#Versio: 1.0
#Descripcio: Numero gran

num1_str = input("Introdueix el primer número: ")
num1 = float(num1_str)

num2_str = input("Introdueix el segon número: ")
num2 = float(num2_str)

num3_str = input("Introdueix el tercer número: ")
num3 = float(num3_str)

num_gran = num1

if num2 > num_gran:
    num_gran = num2

if num3 > num_gran:
    num_gran = num3

print("El número més gran és el ", num_gran)