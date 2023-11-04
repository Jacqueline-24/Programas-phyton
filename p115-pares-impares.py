#Regresa pares e impares de una lista de numeros, usando una funcion

def leer():
    lista=[]
    while True:
        n=float(input("numero: "))
        if n==-1:
            break
        lista.append(n)
    return lista

def paresimpares(lista):
    p=[]
    i=[]
    for n in lista:
        if n%2==0:
            p.append(n)
        else:
            i.append(n)
    return p,i

lista  =leer()
print(lista,len(lista))
p,i=paresimpares(lista)
print("Los pares son ",p,len(p))
print("Los impares son ",i,len(i))



