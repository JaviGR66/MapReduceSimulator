import sys

cantidad = [0, 0, 0]

for item in sys.stdin:
    if int(item) == 1:
        cantidad[0] += 1
    if int(item) == 2:
        cantidad[1] += 1
    if int(item) == 3:
        cantidad[2] += 1

print("Empresa: Electronica Chispas\nAño: 2002\nMes: 11\n\tEnvios tipo 1 --> " + str(cantidad[0]) +
                                                      "\n\tEnvios tipo 2 --> " + str(cantidad[1]) +
                                                      "\n\tEnvios tipo 3 --> " + str(cantidad[2]))
