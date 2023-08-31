# Calcula de un cilindro dado su radio y altura 

import math

print("Calculando el volumen de un cilindro\n")

radio= float(input("Dame el radio?"))
altura= float(input("Dame la altura ?"))

volumen = 3.1416 * (radio * radio) * altura 
volumen = math.pi * math.pow(radio,2) * altura

print(f"Para un cilindro de radio {radio} y altura de {altura} el volumen resultante es {volumen:.2f}")