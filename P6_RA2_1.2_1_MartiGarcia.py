#Cicle: ASIX
#Autor: Martí Garcia
#Data: 25-04-25
#Versio: 1.0
#Descripcio: Numero més gran o no de zero


num_str = input("Introdueix un número: ")

num = float(num_str)

if num > 0:
    print(f" es més gran que zero")
else:
    print(f"{num} no és més gran que zero")