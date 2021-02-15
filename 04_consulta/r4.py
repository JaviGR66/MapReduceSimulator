import sys

from pip._vendor.msgpack.fallback import xrange

proveedor_actual = ""
total_envios = 0
coste = 0
top_coste_envios = [0, 0, 0]
top_proveedores = ["", "", ""]

for item in sys.stdin:

    proveedor, tipo_envio = item.split(";")
    if int(tipo_envio) == 1:
        coste = 10
    if int(tipo_envio) == 2:
        coste = 5
    if int(tipo_envio) == 3:
        coste = 3

    if proveedor != proveedor_actual:
        # if proveedor_actual != "":
        #     print(proveedor_actual + " " + str(total_envios))
        for pos, value in enumerate(top_coste_envios):
            # print("---------------")
            # print(value)
            # print(proveedor_actual)
            # print(total_envios)
            if total_envios >= value:
                # PARA COMPROBAR SI HAY ALGUN OTRO VALOR MENOR
                aux = pos
                new_aux = pos
                while aux <= 2:
                    if value > top_coste_envios[aux]:
                        new_aux = aux
                    aux += 1
                # -----------------------------------------------
                top_proveedores[new_aux] = proveedor_actual
                top_coste_envios[new_aux] = total_envios
                break

        proveedor_actual = proveedor
        total_envios = int(coste)

    else:
        total_envios += int(coste)

# print(proveedor_actual + " " + str(total_envios))
# PARA EL ULTIMO VALOR
for pos, value in enumerate(top_coste_envios):
    if total_envios >= value:
        top_proveedores[pos] = proveedor_actual
        top_coste_envios[pos] = total_envios
        break
# TOP SIN ORDENAR
print(top_proveedores)
print(top_coste_envios)
# TOP ORDENADO
mayor = top_coste_envios[0]
for x in xrange(0, 2):
    if top_coste_envios[x] > mayor:
        a = top_coste_envios.index(mayor)
        b = top_coste_envios.index(top_coste_envios[x])
        mayor = top_coste_envios[x]
        top_coste_envios[a], top_coste_envios[b] = top_coste_envios[b], top_coste_envios[a]
        top_proveedores[a], top_proveedores[b] = top_proveedores[b], top_proveedores[a]
print("TOP 3 GASTOS EN ENVIOS: \n1: "+top_proveedores[0] + " --> " + str(top_coste_envios[0]) + "€"
                              "\n2: "+top_proveedores[1] + " --> " + str(top_coste_envios[1]) + "€"
                              "\n3: "+top_proveedores[2] + " --> " + str(top_coste_envios[2]) + "€")
