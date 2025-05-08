#Cicle: ASIX
#Autor: Martí Garcia
#Data: 06-05-2025
#Versio: 1.0
#Descripcio: 4. Crea un compte bancari i simula 3 operacions: ingrés, retirada vàlida i retirada superior al saldo.

class CompteBancari:
    def __init__(self, saldo):
        self.saldo = saldo

    def Ingressar(self, quantitat):
        self.saldo = self.saldo + quantitat
        
    def Retirar(self, quantitat):
        if quantitat > self.saldo:
            print(f"No es poden retirar els {quantitat} per falta de saldo")
        else:
            self.saldo = self.saldo - quantitat
        
    def Saldo(self):
        print(f"Saldo actual: {self.saldo}")
        
compte = CompteBancari(5000)

print("Ingres: ")
compte.Ingressar(200)
compte.Saldo()

print ("Retirada: ")
compte.Retirar(300)
compte.Saldo()

print ("Retirada Superior: ")
compte.Retirar(4901)
compte.Saldo()

