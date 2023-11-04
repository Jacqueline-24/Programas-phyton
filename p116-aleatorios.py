# Se generan dos listas de numeros aleatorios y se suman
import random

MAX=15

def generaAleatorios():
    l=[]
    for n in range(MAX):
        l.append(random.randint(1,))
    return l

def sumaListas(l1,l2):
    s=[]
    for n in range(MAX):
        s.append(l1[n]+l2[n])
    return s

l1=generaAleatorios()
print("Lista 1 ",l1,len(l1))
l2=generaAleatorios()
print("Lista 2 ",l2,len(l2))
s=sumaListas(l1,l2)
print("La suma de las listas es: ",s,len(s))