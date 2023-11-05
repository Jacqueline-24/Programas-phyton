# Crea una lista y suma los digitos de cada numero
import os 
os.system("cls")

def leer():
    lista=[]
    while True:
        n=int(input("Dame los numeros : "))
        if n==-1:
            break
        lista.append(n)
    return lista

def sumdigitos(lista):
    digito=[]
    for n in lista:
        suma=0
        while n!=0:
            dig=n%10
            suma=suma+dig
            n=n//10
        digito.append(suma)
    return digito    

n=leer()
s=sumdigitos(n)
print(f"La lista de numeros original es: {n}")
print(f"La lista con la suma de digitos de los números es: {s}")
