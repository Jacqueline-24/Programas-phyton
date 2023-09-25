# Imprime los numeros

x = int(input("Desde donde comienza a descender ?"))
y = int(input("De cuanto en cuanto va a descender ?"))

for n in range(x, 0, -y):
    print(n, end=" ")