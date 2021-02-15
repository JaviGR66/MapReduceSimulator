import sys

facturacion = 0
mes_actual = -1
resultado = {}
#
total_anios = 0
dif_anio = []

# OPCION 1 FACTURACION POR MES
# for item in sys.stdin:
#
#     item = item.split(";")
#     money = float(item[1])
#     month = int(item[0])
#
#     if month != mes_actual:
#         if mes_actual != -1:
#             resultado[mes_actual] = facturacion
#
#         mes_actual = month
#         facturacion = money
#     else:
#         facturacion += money
#
# resultado[mes_actual] = facturacion
#
# for k, v in resultado.items():
#     print("Mes: " + str(k) + "\nFacturacion: " + str(v) + "€")

# TODO: ---------------------------------------------------------

# OPCION 2 FACTURACION TOTAL DIVIDIDA EN 12 PARA OBTENER LA MEDIA POR MES

# for item in sys.stdin:
#
#     item = item.split(";")
#     money = float(item[1])
#
#     facturacion += money
#
# print("Facturacion media por mes: " + str(facturacion/12) + "€")

# TODO: ---------------------------------------------------------

# OPCION 3 FACTURACION TOTAL DE CADA MES DIVIDIDA LA CANTIDAD DE AÑOS EN LA QUE LA EMPRESA FACTURO ESE MES

for item in sys.stdin:

    item = item.split(";")
    money = float(item[1])
    month = int(item[0])
    anio = int(item[2])

    if anio not in dif_anio:
        dif_anio.append(anio)
        total_anios += 1

    if month != mes_actual:
        if mes_actual != -1:
            resultado[mes_actual] = facturacion

        mes_actual = month
        facturacion = money
    else:
        facturacion += money

resultado[mes_actual] = facturacion

for k, v in resultado.items():
    print("Mes: " + str(k) + "\nFacturacion: " + str(v/total_anios) + "€")
