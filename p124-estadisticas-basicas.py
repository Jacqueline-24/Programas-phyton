# Lee una lista utilizando funciones de estadistica 

import os 
os.system("cls")
from math import sqrt

def leer():
    lista = []
    while True:
        n = int(input("Dame numeros: "))
        if n == -1 : break
        lista.append(n)
    return lista

def mayor(lista):
    m = lista[0]
    for n in lista:
        if n > m:
            m = n
    return m

def menor(lista):
    m = lista[0]
    for n in lista:
        if n < m:
            m = n
    return m

def media(lista):
    s = 0
    for n in lista:
        s += n
    return s / len(lista)

def varianza(lista):
    media = 0
    for n in lista:
        media += n
    media =  media / len(lista)
    suma = 0
    for n in lista:
        suma += (n - media)**2
    v = (suma * 1 / len(lista))
    return v

def desviacion(lista):
    media = 0
    for n in lista:
        media += n
    media =  media / len(lista)
    suma = 0
    for n in lista:
        suma += (n - media)**2
    varianza = (suma * 1 / len(lista))
    desviacion = sqrt(varianza)
    return desviacion

lista = leer()
print("La lista de numeros es :", lista, len(lista))
media = media(lista)
print(f"La media es: {media:.3f}")
mayor = mayor(lista)
print("El mayor de los datos es:", mayor)
menor = menor(lista)
print("El menor de los datos es:", menor)
var = varianza(lista)
print(f"La varianza es: {var:.3f}")
desv = desviacion(lista)
print(f"La desviación estandar es: {desv:.3f}")