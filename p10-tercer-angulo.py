# Calcular el 3er angulo de un triangulo, dados dos de sus angulos

import math

print("Calculo de un 3er angulo de un triangulo dando dos de sus angulos\n")
print("Dame el angulo1 y el angulo2 en grados separados por un Enter")
angulo1, angulo2 = int(input()), int(input())

angulo3 = 180 - (angulo1 + angulo2)

print(f"El angulo1 de un triangulo es de {angulo1} y el angulo2 es de {angulo2}, da como resultado un angulo3 de {angulo3} ")