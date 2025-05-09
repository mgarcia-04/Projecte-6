#Cicle: ASIX
#Autor: Martí Garcia
#Data: 08-05-2025
#Versio: 1.0
#Descripcio: 3. Termòstat

class Termostat:
    def __init__(self, temperatura_inicial):
        self.__temperatura = temperatura_inicial
        self.temperatura = temperatura_inicial  
    @property
    def temperatura(self):
        return self.__temperatura

    @temperatura.setter
    def temperatura(self, nova_temperatura):
        if 10 <= nova_temperatura <= 30:
            self.__temperatura = nova_temperatura
            print(f"Temperatura ajustada a {self.__temperatura} °C.")
        else:
            print(f"Error: La temperatura ha de ser entre 10 i 30 °C. La temperatura es manté en {self.__temperatura} °C.")

termostat = Termostat(20)

termostat.temperatura = 25
print(f"Nova temperatura: {termostat.temperatura} °C")