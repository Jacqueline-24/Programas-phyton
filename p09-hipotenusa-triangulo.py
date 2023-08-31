# Calcular la hipotenusa de un triangulo rectangulo dadas las longitudes de sus lados

import math

print("Calculando la hipotenusa de un triangulo rectangulo\n")
print("Dame la longlado1 y longlado2 separadas por un Enter")

longlado1 = float(input("Dame la longlado1 ?"))
longlado2 = float(input("Dame la longlad2 ?"))

hipotenusa = math.sqrt ( longlado1 * longlado1 + longlado2 * longlado2)

print(f"La longlado1 de un triangulo rectangulo es de  {longlado1} y longlado2 es de {longlado2} tiene una hipotenusa de {hipotenusa:.2f}")
