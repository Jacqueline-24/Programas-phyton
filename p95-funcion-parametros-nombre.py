# Funcion que al ser invocada usa el nombre del parametro

def saluda(apaterno, amaterno, nombre):
    print(f"Paterno: {apaterno}, Materno: {amaterno}, Nombre: {nombre}")

saluda("Guerrero", "Sanchez","Jacqueline")
saluda(nombre="Jacqueline", apaterno="Guerrero", amaterno="Sanchez")
saluda(amaterno="bernal", nombre="rocio", apaterno="soto")
