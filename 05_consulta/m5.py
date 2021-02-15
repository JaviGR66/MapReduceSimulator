import sys

for line in sys.stdin:
    rows = line.split("\t")

    #comprobrar numero de columnas
    if len(rows) != 9:
        continue
    # espacios al principio y final
    rows = list(map(str.strip, rows))

    # comprobar los numeros

    try:
        rows[0] = int(rows[0])
        rows[2] = int(rows[2])
        rows[3] = int(rows[3])
        rows[4] = int(rows[4])
        rows[8] = float(rows[8])
    except ValueError:
        continue

    year = rows[5].split("/")[2]
    if int(year) != 2005:
        continue

    print(rows[1] + ";" + str(rows[8]))
