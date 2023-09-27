# Imprime el factorial de un numero
import os

os.system("cls")
n = int(input("Dame el numero del cual deseas el factorial ?"))
f = 1
for h in range(1,n+1):
    print(h, end="*")
    f = f * h

print(" = ", f)
