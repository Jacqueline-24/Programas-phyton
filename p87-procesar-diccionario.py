# Ingresa datos de nombres y sueldos en un diccionario
import os 
os.system("cls")

nombres = ["Juan", "Pedro", "Manuel", "Elias", "Maria", "Felipe", "Julia", "Roberto"]
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]


trabajadores = dict(zip(nombres, sueldos))
print("Diccionario resultante:", trabajadores)

print("\nLas llaves :")
for k in trabajadores.keys():
    print(k, end=" ")


print("\nLos valores:")
for v in trabajadores.values():
    print(v, end=" ")


print("\nLlaves y valores a la vez :")
for k, v in trabajadores.items():
    print(k, "-", v)

print("Diccionario utilizando items():")
for nombre, sueldo in trabajadores.items():
    print(nombre, "-", sueldo)

s=p=0
for m, c in trabajadores.items():
    print(f"{m:<12} - {c}")
    s = s + c
p = s / len(trabajadores)
print(f"La suma es {s} y el promedio {p}");