# Obtener el numero de la suerte con la suma de los digitos individuales del año de nacimiento

print("Dividir el año de nacimiento en 4 cifras\n")

numero = int(input("Dame un numero entero de 4 cifras ?"))

millares = numero // 1000
centenas = (numero - millares*1000)// 100
decenas = (numero - millares * 1000 - centenas*100) // 10
unidades = numero - (millares*1000 + centenas*100 + decenas * 10)


print(f"Millares: {millares}\nCentenas: {centenas}\nDecenas: {decenas}\nUnidades: {unidades}")
print(f"Numero de la suerte {millares+centenas+decenas+unidades}")