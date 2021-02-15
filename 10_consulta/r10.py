import sys

balance = 0

for item in sys.stdin:
    balance += float(item)

print("Balance de factuacion de Madrid" + str(balance))
