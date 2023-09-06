# Muestra el tipo de angulo
# <90 agudo, =90 recto, <90 y <180 obtuso, =180 llano, >180 y <360 concavo, =360 completo

angulo = int(input("Dame el angulo ?"))

if angulo>= 0 and angulo <= 360:
    print("continuar")
    if angulo < 90:
        print("agudo")
    elif angulo == 90:
        print("recto")
    elif angulo>90 and angulo<180:
        print("obtuso")
    elif angulo==180:
        print("llano")
    elif angulo>180 and angulo<360:
        print("concavo")
    else:
        print("completo")
else:
    print("angulo fuera de rango")
