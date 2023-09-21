# Imprimir los números pares desde 100 hasta el número que el usuario decida (n),imprimir tambien la suma de esos números pares

import os

while(True):

    os.system("cls")
    c = 100
    sum = 0
    n = int(input("Hasta que numero desea llegar ?"))
    while c >= n:
        print(c, end=" ")
        sum += c
        c -= 2

    print(f"\nLa suma de los numeros pares es: {sum}")

    resp = input("Deseas continuar (S/N) ?")
    if resp =="N":
        break 

print("\nProceso terminado...")
    