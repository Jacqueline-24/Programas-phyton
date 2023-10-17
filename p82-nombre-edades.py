datos = {}

print("Introduce nombres y edades, * en el nombre para terminar")
while True:
    nombre = input("Nombre :")
    if nombre == "*":
        break
    else:
        datos[nombre] = int(input("Edad :"))

print("\nLos datos introducidos son:\n", datos, len(datos))

s=p=0
for n, e in datos.items():
    print(f"{n:<20} - {e:3}")
    s = s + e
p = s / len(datos)
print(f"\nLa suma : {s} y el promedio : {p:.2f}")