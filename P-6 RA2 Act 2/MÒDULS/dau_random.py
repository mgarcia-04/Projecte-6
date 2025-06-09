import random

def llençar_dau():
    return random.randint(1, 6)

def simula_daus(n):
    resultats = [llençar_dau() for _ in range(n)]
    return sum(resultats) / n

print("Mitjana de 100 tirades:", simula_daus(100))
