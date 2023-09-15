# Dados tres números enteros, verifica cual es el mayor

print("\nVerifica cua es el numero mayor de tres numeros entero")
print("Dame tres numero enteros ?")

n1, n2, n3 = input().split()
n1, n2, n3 = (int(n1), int(n2), int(n3))

if  n1 > n2 or n1 > n3:
    print(f"El numero mayor es {n1}")

elif n2 > n2 or n2 > n3:
    print(f"El numero mayor es {n2}")

elif n3 > n1 or n3 > n2:
    print(f"El numero mayor es {n3}")

print("\nProceso terminado")