def es_parell(numero):
    return numero % 2 == 0

llista_nombres = [1, 2, 3, 4, 5, 6]
for num in llista_nombres:
    print(f"El número {num} és parell: {es_parell(num)}")