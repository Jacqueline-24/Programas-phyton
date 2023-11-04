# Crea un modulo con las funciones
def menor(lista):
    m=lista[0]
    for n in lista:
        if n<m:
            m=n
    return m

def mayor(lista):
    m=lista[0]
    for n in lista:
        if n>m:
            m=n
    return m

def promedio(lista):
    s=0
    for n in lista:
        s+=n
    return s/len(lista)

def suma(lista):
    s=0
    for n in lista:
        s+=n
    return s

def leer():
    lista=[]
    while True:
        n=float(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista
