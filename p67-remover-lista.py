# Cree una lista con los siguientes elementos: 100, 123, 456, 222, 999, 895, 325, 234, 322, 988. Después remover elementos
import os

os.system("cls")

num = [100, 123, 456, 222, 999, 895, 325, 234, 322, 988]
print(num, len(num))

remover = [100, 123, 456]
for n in remover:
    if n in num:
        num.remove(n)
print(num, len(num))
num.remove(322)
print(num, len(num))
num.remove(988)
print(num, len(num))
remov = num.pop(0)
print(num, len(num))
print("El elemento removido es :", remov)
remov = num.pop(3)
print(num, len(num))
print("El elemento removido es :", remov)

print("La lista resultante es : ", num)

num.clear()
print(num, len(num))



