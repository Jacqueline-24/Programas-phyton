# Crear un programa que permita procesar una lista de n números enteros
import os
os.system("cls")

n = int(input("Cuantos números ? "))
nums = []

for i in range(n):
    num = int(input("Ingrese un número entero: "))
    nums.append(num)

print(f"La lista de números ingresados es:", nums)

suma = sum(nums)
print()
prom = suma / n

print("La suma de los números es:", suma)
print("El promedio de los números es:", prom)