# Aceptar a un estudiante en base a la edad y sus calificaciones 
import os 

os.system("cls")
nombre = input("\nDame tu mombre ?")
edad = int(input("Dame tu edad ?"))
           
if edad>=18 :
    print("continuamos...")
    print("Dame 2 calificaciones separados por un Enter")
    c1, c2 = int(input()), int(input())
    if c1>=8 and c2>=8:
        print(f"{nombre} bienvenid@ tus calificaciones son {c1} y {c2}")
    else:
        print("Solo aceptamos calificaciones mayores a 8")
else:
    print("Solo aceptamos mayores de 18")

print("\nProceso terminado...")
    
