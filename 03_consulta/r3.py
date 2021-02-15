import sys

facturacion = 0
ano_actual = 0
resultado = {}
#
facturacion_anterior = 1

for item in sys.stdin:

    item = item.split(";")
    money = float(item[1])
    year = int(item[0])
    if year != ano_actual:
        if ano_actual != 0:
            resultado[ano_actual] = facturacion

        ano_actual = year
        facturacion = money
    else:
        facturacion += money

resultado[ano_actual] = facturacion

for k, v in resultado.items():
    print("Año: " + str(k) + "\nFacturacion: " + str(v) + "€\nIncremento de facturacion: " + str(int(100*(v/facturacion_anterior))-100) + "%")
    facturacion_anterior = v
