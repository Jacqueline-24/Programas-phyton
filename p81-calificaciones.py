
materias = ["Fisica", "Quimica", "Matematicas", "Geografia", "Estadistica"]
califis  = [10, 9, 8, 7.5, 6]
print("Lista de materias        : ", materias)
print("Lissta de calificaciones : ", califis)
notas = dict(zip(materias,califis))
print("\nLas notas : ", notas, len(notas))
notas.update({"Ingles" : 10})
notas.update({"Programacion" : 7})
print("\nDiccionario actualizado : ", notas, len(notas))
notas.pop("Fisica")
notas.popitem()
print("\nDiccionaro actualizado :", notas, len(notas))
notas.update({"Quimica": 10})
notas.update({"Matematicas": 10})
print("\nDiccionario actualizado :", notas, len(notas))
s=p=0
for m, c in notas.items():
    print(f"{m:<12} - {c}")
    s = s + c
p = s / len(notas)
print(f"La suma es {s} y el promedio {p}");
