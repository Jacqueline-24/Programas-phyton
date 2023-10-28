# Numero menor 

def menor(n1, n2, n3):
    if n1 <= n2 and n1 <= n3:
        return n1
    elif n2 <= n1 and n2 <= n3:
        return n2
    else:
        return n3

# Programa principal
print("Dame 3 numeros :")
n1,n2,n3 = int(input()),int(input()),int(input())
men = menor(n1,n2,n3)
print(f"El menor de los tres numeros es {men}")
