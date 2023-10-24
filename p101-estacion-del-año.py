# Regresa la estacion del año con letra dado un numero del 1 al 4

def estacion(n):
    est = ""
    if n==1:
            est = "Primavera"
    elif n==2:
            est = "Verano"
    elif n==3:
            est ="Otoño"
    elif n==4:
            est = "Invierno"
    else:
            est = "Error"
    return est

n = int(input("Dame la estacion del año (1-4) ?"))
print(f"La estacion del año es { estacion(n) }")