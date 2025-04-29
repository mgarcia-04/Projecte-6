#Cicle: ASIX
#Autor: Martí Garcia
#Data: 29-04-25
#Versio: 1.0
#Descripcio: Fibonacci

a, b = 0, 1

print("Els primers 10 termes de la seqüència de Fibonacci són:")

for _ in range(10):
  print(a, end=" ")
  a, b = b, a + b

print()