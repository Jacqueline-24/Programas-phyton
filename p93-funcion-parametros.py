# Funcion con varios parametros

def saluda(nombre, edad, telefono, correo):
    print("*"*120)
    print(f"Bienvenido {nombre} tu edad es {edad}, tu telefono es {telefono}, tu correo es {correo}", end="")
    if(edad>=18): print("eres mayor de edad")
    else: print("eres menor de edad")
    print("*"*120)
    print()

saluda("Carlos Castaneda", 51, "4928920916", "castr@uaz.edu.mx")
saluda("Carlos Antonio", 14,"4921042567", "charly@msn.com")
