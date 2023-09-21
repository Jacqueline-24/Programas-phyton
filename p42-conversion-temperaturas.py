# Calcular la temperatura convertida de grados centígrados a grados farenheit de un rango de valores introducidos por el usuario

import os

while(True):
    os.system("cls")
    temi = float(input("Dame la temperatura inicial ?"))
    temf = float(input("Dame la temperatura final ?"))
    c = temi
    print("°C\t°F")
    print("-" * 15)
    while c <= temf :
        print(f"{c}\t{(c * 9/5) + 32:.2f}")
        c += 1
    print("-" * 15)
    resp = input("Deseas continuar (S/N) ?")
    if resp =="N": break 

print("\nProceso terminado...")

