# Imprime las tablas del 1 a n, desde 1 hasta m

import os 

os.system("cls")

n= int(input("Hasta que tabla quieres ?"))
m = int(input("Hasta donde ?"))

for i in range(1,n+1):
    print(f"\nTabla del {i}\n")
    for j in range(1,m+1):
        print(f"{i} x {j} = {i * j}")