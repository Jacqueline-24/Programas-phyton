# Funcion que recibe un numero arbitrario de parametros

def saludosatodos(*todos):
    print("Saludos a", todos)
    for nombre in todos:
        print("Hola", nombre)
    if(len(todos)!=0):
        print("El primero es el primero y es ", todos[0])
        print("El ultimo es el ultimo y es ", todos [-1])


saludosatodos("Juan", "Pedro", "Luis", "Jose")