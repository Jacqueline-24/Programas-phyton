# Im
import os
while(True):
    
    os.system("cls")
    n= int(input("Hasta que tabla ?"))
    m = int(input("Hasta donde ? "))
    t = 1
    while t <= n :
        print(f"\nTabla del {t}\n")
        c=1
        while c <= m :
            print(f"{t} x {c} = {t*c}")
            c = c + 1
        t = t + 1

    resp = input("Deseas continuar (S/N) ?")
    if resp =="N": break 

print("\nProceso terminado...")
