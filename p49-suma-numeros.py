# Imprimir la suma y el promedio de n numeros introducidos por el usuario
import os 

while(True):
    os.system("cls")
    n = int(input("Cuantos numeros deseas procesar ?"))
    suma = 0
    promedio = 0

    for c in range(1, n+1):
        num = int(input(f"Numero {c} ?"))
        suma = suma + num

    promedio = suma / n
    print("\nLa suma es: ", suma)
    print("\nEl promedio es: ", promedio)

    resp = input("\nDeseas continuar (S/N) ?").upper()
    if resp=="N": break
print("\nProceso terminado...")