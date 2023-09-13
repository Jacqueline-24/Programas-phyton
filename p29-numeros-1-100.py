# Imprimir los numeros del 1 al 100 de 1 en 1 

n = int(input("Hasta donde deseas llegar ?"))
p = int(input("De cuanto en cuanto ?"))

c = 1
while c <= n :
    print(c, end= " ")
    c = c + p

