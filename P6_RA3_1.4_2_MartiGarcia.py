#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 2. Refés el codi perquè la classe Comanda no depengui d’una implementació concreta del notificador

class Comanda:
    def __init__(self, client, notificador):
        self.client = client
        self.notificador = notificador

    def confirmar(self):
        print(f"Comanda confirmada per {self.client}")
        self.notificador.enviar(f"Hola {self.client}, la teva comanda ha estat confirmada.")