# Calcular el número mayor de una serie de números introducidos por el teclado, el proceso se detiene al introducir 0

import os


while(True):
    os.system("cls")
    nmay=0
    while(True):
        n =int(input("Introduce los numeros ?"))
        if n == 0:
            break
        if n > nmay:
            nmay = n
            print(f"El numero mayor es : {nmay}")

    resp = input("Deseas continuar (S/N) ?").upper()
    if resp == "N": break
print("Proceso terminado...")