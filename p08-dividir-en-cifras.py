# Dividir un numero entero de 3 cifras, en centenas, decenas y unidades
# 491

print("Dividir un numero entero de 3 cifras, en centenas, decenas y unidades\n")

numero = int(input("Dame un numero entero de 3 cifras ?"))

centenas = numero // 100
decenas = (numero - centenas*100) // 10
unidades = numero - (centenas*100 + decenas * 10)


print(f"Centenas: {centenas}\nDecenas: {decenas}\nUnidades: {unidades}")
print(f"Suma digitos {centenas+decenas+unidades}")


