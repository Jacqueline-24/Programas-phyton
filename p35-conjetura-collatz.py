# Calcula e imprime los numeros de la conjetura de collaz
import os

while (True):

    os.system("cls")
    while(True):
        num = int(input("Dame un entero positivo: "))
        if num > 0: break

    while( num != 1) :
        print(num, end="")
        if num % 2 == 0:
                num = num // 2
        else :
                num = num * 3 +1
    print(num, end="")

    res = input("\nDeseas continuar (S/N) ?").upper()
    if res =="N": break

print("\nProceso terminado...")