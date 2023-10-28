# Imprime la funcion de suma de pares e impares de un rango de numeros

def sumaparesimpares(ini, fin):
    spar = 0
    simpar = 0
    pares = []
    impares = []
    for i in range(ini, fin+1):
        if i % 2 == 0 : 
            pares.append(i)
            spar += i
        else: 
            impares.append(i)
            simpar += i
    return pares, impares, spar, simpar

# Programa principal
print("[ P ] ares")
print("[ I ] impares")
op = input("Elige ? ").upper()
if op == "P":
    ini = int(input("Desde que numero ?"))
    fin = int(input("Hasta que numero? "))
    pares, impares, spar, simpar = sumaparesimpares(ini, fin)
    print(f"Los numeros pares sumados son: {pares}")
    print(f"La suma es: {spar}")
elif op == "I":
    ini = int(input("Desde que numero ?"))
    fin = int(input("Hasta que numero? "))
    pares, impares, spar, simpar = sumaparesimpares(ini, fin)
    print(f"Los numeros impares sumados fueron {impares}")
    print(f"La suma de los numero fue {simpar}")
else:
    print("Opcion incorrecta")