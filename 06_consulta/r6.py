import sys

cantidad_envios = 0
peso_total = 0
volumen_total = 0

for item in sys.stdin:
    peso, volumen = item.split(";")
    peso_total += int(peso)
    volumen_total += int(volumen)
    cantidad_envios += 1


print("Numero total de envios: " + str(cantidad_envios) +
      "\nDensidad Total --> " + str(peso_total/volumen_total) + " kg/m^3"
      "\nDensidad Media --> " + str((peso_total/volumen_total)/cantidad_envios) + " kg/m^3")
