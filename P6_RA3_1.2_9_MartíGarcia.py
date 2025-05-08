#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. 9. Crea una classe Llibre

class Llibre:
    def __init__(self, titol, autor, any):
        self.titol = titol
        self.autor = autor
        self.any = any

    def mostrar_info(self):
        print(f"Titol: {self.titol}\nAutor: {self.autor}\nAny publicació: {self.any}")

informacio = Llibre("El señor dee los anillos", "J. R. R. Tolkien", 1954)
informacio.mostrar_info()