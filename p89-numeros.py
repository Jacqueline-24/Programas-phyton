# Conjuntos de numeros
import os
os.system("cls")

A = {50, 60, 70, 80, 90, 100, 200}
B = {60, 90, 100, 300, 400, 500}
C = {10, 20, 60, 90, 70, 100, 600, 700}

print(A)
print(B)
print(C)

print("\nUnion")
print("A union B",A.union(B))

print("\nUnion")
print("B union C",B.union(C))

print("\nDiferencia")
print("A diferencia C",A.difference(C))

print("\nDiferencia simetrica")
print("B dif simetrica C", B ^ C)

print("\nInterseccion")
print("B interseccion C",B & C)

print("\nComprobamos subconjuntos")
print("A es subconjunto B", A.issubset(B))

print("\nComprobamos subconjuntos")
print("C es subconjunto A", C.issubset(A))

print("\nVerificar")
print("100 esta en A", 100 in A)

print("\nVerificar")
print("60 esta en A", 60 in A)
print("60 esta en B", 60 in B)
print("60 esta en C", 60 in C)

print("\nVerificar")
print("900 no esta en C", 900 is not C)
