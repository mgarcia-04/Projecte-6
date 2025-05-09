#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 9. Gestor de puntuació

class Joc:
    def __init__(self):
        self.__puntuacio = 0

    @property
    def get_punts(self):
        return self.__puntuacio
    
    def sumar_punts(self, nova_puntuacio):
        print(f"La puntuació actual és: {self.__puntuacio}")
        self.__puntuacio = self.__puntuacio + nova_puntuacio
        print(f"En aquesta partida s'han guanyat {nova_puntuacio}, sumant un total de {self.__puntuacio} punts")
        return self.__puntuacio
    
    def reiniciar_punts(self):
        print("S'ha reiniciat la partida!")
        self.__puntuacio = 0
    
puntuacio = Joc()

puntuacio.sumar_punts(30)

puntuacio.sumar_punts(40)

puntuacio.reiniciar_punts()

puntuacio.sumar_punts(120)
    
    
