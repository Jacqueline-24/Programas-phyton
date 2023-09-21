# Imprima los números impares de forma ascendente desde 1 hasta el número que el usuario decida (n), imprimir tambien la suma de esos números impares

import os
while(True):
    
    os.system("cls")
    c = 1
    sum = 0
    n = int(input("Hasta que nuemero desea llegar ?"))

    while c <= n:
        print(c, end =" ")
        sum += c
        c += 2

    print(f"\nLa suma de los numeros impares es : {sum}")

    resp = input("Deseas continuar (S/N) ?")
    if resp =="N":break 

print("\nProceso terminado...")
