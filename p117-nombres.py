# Procesar una lista de nombres, junta una lista original con una lista introducida por el usuario

def procesa(n1,n2):
    res = []
    res.extend(n1)
    res.extend(n2)
    res.sort(reverse=True)
    for n in range(len(res)):
        res[n] = res[n].upper()
    return res

def leer():
    d = []
    while True:
        n = input("Nombre ?")
        if n=="**": break
        d.append(n)
    return d

nombres1 = ["Juan","Pedro","Luis","Jose","Maria"]
#nombres2 = ["Lucia","Angelica,"Miguel"]
nombres2 = leer()

print("Lista de nombres 1:", nombres1, len(nombres1))
print("Lista de nombres 2:", nombres2, len(nombres2))

todos = procesa(nombres1,nombres2)

print("Lista de todos :", todos, len(todos))