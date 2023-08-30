# Convierte grados celcius a grados farenheit y viceversa

print("Convierte grados celcius a grados farenheit y viceversa\n")
opcion = str.upper (input("[C]entigrados a Farenheit\n[F]arenheit a Centigrados\nElige ?"))
# opcion = str.upper{opcion}

if opcion == "C" :
    print("\nConvirtiendo de Farenheit a Centigrados")
    temp = float(input("Grados Farenheit ?"))
    res  = (temp - 32) * 5 / 9
    print(f"{temp} grados farenheit equivalen a {res:.2f} grados centigrados")
else:
    print("\nConvirtiendo de Centigrados a Farenheit")
    temp = float(input("Grados Centigrados ? "))
    res  = (temp * 9 / 5) + 32
    print(f"{temp} grados centigrados equivalen a {res:.2f} grados farenheit")

print("\nProceso Terminado...")