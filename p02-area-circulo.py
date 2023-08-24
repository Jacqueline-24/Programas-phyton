# Calcula el area de un circulo dado el radio

import math #importamos la libreria de funciones y constantes matematicas

print("Calculando el area de un circulo/n")

radio= float(input("Dame el radio?"))

area= 3.1416 * radio * radio 
area= math.pi * math.pow(radio,2)

print(f"Para un circulo de radio {radio} el area resultante es {area:.2f}")

