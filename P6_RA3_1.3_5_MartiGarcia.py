#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 5. Sensor amb valors limitats

class Sensor:
    def __init__(self, valor_inicial):
        self.__valor = 0
        self.valor = valor_inicial

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, nou_valor):
        if 0 <= nou_valor <= 100:
            self.__valor = nou_valor
            print(f"Valor del sensor actualitzat a {self.__valor}.")
        else:
            print(f"Error: El valor del sensor ha de ser entre 0 i 100. El valor es manté en {self.__valor}.")

sensor = Sensor(0)
print(f"Valor inicial del sensor: {sensor.valor}")

sensor.valor = 55
print(f"Nou valor del sensor: {sensor.valor}")
