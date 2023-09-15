# Calcula el promedio de 5 calificaciones dadas por un usuario y evalua el resultado del promedio obtenido

print("\nCalcula el promedio de 5 calificacion ")
print("Dame el valor de las cinco calificaciones ?")

c1, c2, c3, c4, c5 = int(input()), int(input()), int(input()), int(input()), int(input())
s = c1 + c2 + c3 + c4 +c5
prom = s / 5

if prom <= 6:
    print(f"El promedio es de {prom} quedas reprobado")
elif prom > 6 and prom <= 7:
    print(f"El promedio es de {prom} pasas de panzazo")
elif prom > 7 and prom <= 8:
    print(f"El promedio es de {prom} muy bien, puedes mejorar")
elif prom > 8 and prom <= 9:
    print(f"El promedio es de {prom} excelente sigue así")
elif prom > 9 and prom <= 10:
    print(f"El promedio es de {prom} perfecto tu esfuerzo valió la pena")

else:
    print("La calificacion no se encuentra en el rango")

