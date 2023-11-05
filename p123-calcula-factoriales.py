# Crea una lista de numeros y calcula el factorial
import os 
os.system("cls")

def leer():
    lista=[]
    while True:
        n=int(input("Dame los numeros :"))
        if n==-1:
            break
        lista.append(n)
    return lista

def factorial(lista):
    fact=[]
    for n in lista:
        f=1
        for n in range(1,n+1):
            f=f*n
        fact.append(f)
    return fact

n=leer()
f=factorial(n)
print(f"La lista de números originales es: {n}")
print(f"La lista con los factoriales es: {f}")