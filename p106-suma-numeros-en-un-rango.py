# Suma números en un rango

def sumarango(ini, fin):
    sum = 0
    for i in range(ini, fin+1):
        sum += i
    return sum

# Programa principal
n1 = int(input("Desde que numero ?"))
n2 = int(input("Hasta que numero ?"))
print(f"La suma de los numeros es: {sumarango(n1,n2)}")