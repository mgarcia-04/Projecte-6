#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 20. Demana una llista de paraules i crea una nova llista amb només les paraules que comencen per vocal.

paraules = []
num_paraules = int(input("Quantes paraules vols introduir? "))
for i in range(num_paraules):
    paraula = input(f"Introdueix la paraula {i+1}: ")
    paraules.append(paraula)

vocals = "aeiouAEIOU"
paraules_amb_vocal = [paraula for paraula in paraules if paraula[0] in vocals]
print("Les paraules que comencen per vocal són:", paraules_amb_vocal)