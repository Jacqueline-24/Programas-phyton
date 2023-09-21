# Calcular la suma de números introducidos por el usuario hasta que la suma sea >= 200, luego mostrar cuantos números fueron introducidos y la suma de estos
import os

while(True):
    os.system("cls")
    lim = 0
    num = 0   
    sum = 0   

    while lim < 200:
        c = int(input("Introduce un numero ?"))
        lim += c
        num += 1
        sum += lim
        print(lim, end=" ")
    print(f"\nNumeros introducidos {num}")
    print(f"\nLa suma alcanzada es de {lim}")
    print(f"\nLa suma de los numeros que se introdujeron es de {sum}")

    resp = input("Deseas continuar (S/N) ?")
    if resp =="N": break 

print("\nProceso terminado...")
        