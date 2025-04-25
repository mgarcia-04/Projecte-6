import math

PI = 3.1416 # Constant: PI

def calcular_area(radi): # Funció: calcular_area
  return PI * radi ** 2

radi = float(input("Introdueix el radi: ")) # Línia que llegeix dades de l'usuari
# Variables: radi
area = calcular_area(radi) # Variable: area
print("L'àrea del cercle és:", area) # Línia que mostra el resultat