# Dados tres números enteros, verificar si son consecutivos (9,10,11) o si no lo son (1,4,6)

print("\nVerificar si tres numeros son consecutivos o no")
print("Dame tres numeros enteros ?")

n1, n2, n3 = input().split()
n1, n2, n3 = [ int(n1), int(n2), int(n3)]

if n1 + 1 == n2 and n1 + 2 == n3: 
    print("Los numeros son consecutivos")
else:
    print("Los numeros no son consecutivos")

print("\nProceso terminado")