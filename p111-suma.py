# Calcula la suma de una lista de numeros usando una funcion

#funcion
def suma(lista):
    s=0
    for n in lista:
        s+=n
    return s

# principal
#lista=[10,20,30,40,50]

lista=[]
while True:
    n=float(input("numero: "))
    if n==-1:
        break
    lista.append(n)

print(lista,len(lista))
res=suma(lista)
print("La suma es ",res)