# Imprime los numeros de 1 a n o de n a 1, segun el usuario lo decida

import os

while(True):
    os.system("cls")
    print("[1] Imprimir los numeros de 1 a n")
    print("[2] Imprimir los numeros de n a 1")
    op = int(input("Elige ?"))

    if op==1:
        print("\nImprimiendo de 1 hasta n\n")
        n= int(input("Dame el valor de n ?"))
        for z in range(1, n+1):
            print(z, end=" ")
    elif op==2:
        print("\nImprimiendo de n ?")
        n = int(input("Dame el valor de n ?"))
        for w in range(n, 0, -1):
            print(w, end=" ")
    else:
        print("\nOpcion invalida")
    resp = input("\Deseas continuar (S/N) ?").upper()
    if resp =="N": break
print("Proceso terminado...")
