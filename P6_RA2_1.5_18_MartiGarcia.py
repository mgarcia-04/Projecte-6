#Cicle: ASIX
#Autor: Martí Garcia
#Data: 30-04-25
#Versio: 1.0
#Descripcio: 18. Escriu una funció que retorni la llista al revés (sense reverse()).

def invertir_llista(llista):
    llista_invertida = []
    for i in range(len(llista) - 1, -1, -1):
        llista_invertida.append(llista[i])
    return llista_invertida

nombres = [10, 20, 30, 40, 50]
nombres_invertits = invertir_llista(nombres)
print("La llista invertida és:", nombres_invertits)