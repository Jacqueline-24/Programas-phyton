# Verifica si la suma de dos numeros es igual a un tercero

print("Verifica si la suma de dos numeros es igual a un tercero\n")
print("Dame 3 numeros enteros : ")

n1, n2 , n3 = int(input()), int(input()), int(input())

if n1 + n2 == n3 :
    print("Son iguales")
else:
    print("Son distintos")

print("\nProceso terminado")