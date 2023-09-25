# Imprime los numeros del 1 al x con for

x = int(input("Hasta donde ?"))
y = int(input("De cuanto en cuanto ? "))

for n in range(1, x+1, y):
    print(n, end=" ")