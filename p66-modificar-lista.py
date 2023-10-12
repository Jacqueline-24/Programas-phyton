# Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988. Después modifique elementos
import os
os.system("cls")

num = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]

print(num, len(num))
print(type(num))
num[0] = 200
print(num)
num[4] = 1000
print(num)
num[9] = 999
print(num)
num[1:4] = [555,666,777]
print(num)

lista = print(f"\nLa lista resultante : {num}")
