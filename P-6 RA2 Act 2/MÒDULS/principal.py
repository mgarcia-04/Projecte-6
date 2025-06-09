import calculadora
import conversions
import geometria
import textos as tx
import cientifica
import constants
from utilitats import temps, moneda

print(calculadora.suma(3, 5))
print(conversions.celsius_a_fahrenheit(25))
print(geometria.area_quadrat(4))
print(tx.capitalitza("hola món"))
print(cientifica.arrel(16))
print("Força gravitatòria:", 70 * constants.GRAVETAT)
print(temps.segons_a_hores(3600))
print(moneda.euros_a_dolars(100))
