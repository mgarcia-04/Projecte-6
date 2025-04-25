distancia_km = float(input("Introdueix la distància en quilòmetres: "))
temps_hores = float(input("Introdueix el temps en hores: "))

if temps_hores > 0:
  velocitat_mitjana = distancia_km / temps_hores
  print("La velocitat mitjana és de:", velocitat_mitjana, "km/h")
else:
  print("El temps no pot ser zero o negatiu.")