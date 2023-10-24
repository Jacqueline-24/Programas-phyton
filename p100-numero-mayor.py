#Determina el mayor de tres numeros 

def mayor(n1,n2,n3):
    may = 0
    if n1>n2 and n1>n3:
        may = n1
    elif n2>n3 and n2>n3:
        may = n2
    else :
        may = n3
    return may

# Programa principal
print("Dame 3 numeros :")
n1,n2,n3 = float(input()),float(input()),float(input())
may = mayor(n1,n2,n3)
print(f"El mayor de los tres numeros es {may}")