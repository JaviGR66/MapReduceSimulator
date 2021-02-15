import sys

facturacion = 0

for item in sys.stdin:
    facturacion += float(item)

print("Facturacion total: " + str(facturacion) + "€")
