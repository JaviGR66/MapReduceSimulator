import sys

ciudad_actual = ""
cont = 0
ciudad_max = ""
valor_max = 0

for item in sys.stdin:
    if item != ciudad_actual:
        if ciudad_actual != "":
            if valor_max < cont:
                ciudad_max = ciudad_actual
                valor_max = cont

        ciudad_actual = item
        cont = 1
    else:
        cont += 1

if valor_max < cont:
    ciudad_max = ciudad_actual
    valor_max = cont

print("Ciudad con mas envios --> " + ciudad_max + "\nCantidad de envios --> " + str(valor_max))
