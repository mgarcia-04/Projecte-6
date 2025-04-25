# a. Una constant
SALUTACIO = "Hola!"

# b. Una funció
def saludar(nom):
  missatge = SALUTACIO + " " + nom
  return missatge

# c. Una entrada de l'usuari
nom_usuari = input("Com et dius? ")

# d. Una sortida per pantalla
salutacio_final = saludar(nom_usuari)
print(salutacio_final)