# Imprime una piramide de un caracter determinado usando dos ciclos for anidados
import os 

os.system("cls")
n = int(input("Cuantos renglones ?"))
c = input("Caracter ? ")
for i in range(1,n+1):
    for j in range(1,i+1):
        print(c, end="")
    print()