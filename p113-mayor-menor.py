# Calcular el mayor y el menor de una lista de numeros, usando funciones

def leer():
    lista=[]
    while True:
        n=float(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

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

lista =leer()
print(lista,len(lista))
men=menor(lista)
print("El menor es: ", men)
may=mayor(lista)
print("El mayor es: ",may)