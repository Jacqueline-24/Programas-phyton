# Ingresar listas de nombres
import os 
os.system("cls")

lista1 = ["Juan", "Maria", "Pedro", "Jose", "Rocio"]
lista2 = ["Pedro", "Juan", "Pablo", "Mateo", "Esther"]

A = set(lista1)
B = set(lista2)
print("Conjunto A:", A)
print("Conjunto B:", B)

print("\nUnion")
print("A union B",A.union(B))

print("\nInterseccion")
print("A interseccion B",A & B)

print("\nDiferencia")
print("A diferencia B",A - B)

print("\nDiferencia simetrica")
print("A dif simetrica B", A ^ B)

print("\nComprobamos subconjuntos")
if {"Pablo", "Mateo"}.issubset(B):
    print("El conjunto de nombres [Pablo, Mateo] es subconjunto de B")
else:
    print("El conjunto de nombres [Pablo, Mateo] no es subconjunto de B")

print("\nComprobar superconjunto")   
if A.issuperset({"Reynaldo", "Angelica"}):
    print("A es superconjunto del conjunto de nombres [Reynaldo, Angelica]")
else:
    print("A no es superconjunto del conjunto de nombres [Reynaldo, Angelica]")


print("\nVerificar")
print("Pedro no esta en A", not A)
print("Pedro si esta en A", "Pedro" in A)

print("\nVerificar")
print("Lilia no esta en B", "Lilia" is not B)
print("Lilia si esta en B", "Lilia" in B)