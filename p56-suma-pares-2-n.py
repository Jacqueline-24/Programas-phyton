# Imprima los pares de 2 a n y su suma 
import os


os.system("cls")

num = int(input("Dame un numero ?"))
suma = 0

for i in range(2,num+1,2):
    print(i,end=" ")
    suma += i
print(f"\nLa suma es: {suma}")