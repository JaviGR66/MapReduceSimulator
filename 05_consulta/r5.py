import sys

lista_precios = [0, 9999]
# Es lo mismo que crear dos variable que sea mayor y menor pero lo hago asi para tener tambien en
# una lista el nombre de los proveedores
lista_proveedores = ["", ""]

for item in sys.stdin:

    item = item.split(";")
    money = float(item[1])
    proveedor = item[0]
    if money > lista_precios[0]:
        lista_precios[0] = money
        lista_proveedores[0] = proveedor
    if money < lista_precios[1]:
        lista_precios[1] = money
        lista_proveedores[1] = proveedor

print("Año 2002: \nVenta mas cara: " + str(lista_precios[0]) + "\tEmpresa: " + lista_proveedores[0] +
      "\nVenta mas barata: " + str(lista_precios[1]) + "\tEmpresa: " + lista_proveedores[1])

