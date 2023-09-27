# Imprimir la tabla de multiplicar que el usuario decida usando un ciclo for

import os

while(True):
    os.system("cls")

    t = int(input("Que tabla deseas ?"))
    n = int(input("Hasta donde ?"))

    for i in range(1, n+1):
        print(f"{t} x {i} = {t*i}")

    resp = input("\nDeseas continuar (S/N) ?").upper()
    if resp =="N": break
print("\nProceso terminado...")