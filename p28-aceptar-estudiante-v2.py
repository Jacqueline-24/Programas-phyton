# verifica si el estudiante es aceptado dado el nombre del estudiante, sexo (h/m), su edad y tres calificaciones

print("Verificar que un estudiante puede ser aceptado en la Universidad Kitty Kat SA que es solo para mujeres, cuenta con 21 años y tiene un promedio entre 8 y 9.5")

nombre = input("\nDame tu mombre completo?")
print("[H]ombre")
print("[M]ujer")
sexo = input("Dime tu sexo H/M ? ").upper()

if sexo == "M" :
    edad = int(input("Dame tu edad ?"))
    if edad>=21 :
        print("Dame 3 calificaciones separados por un Enter")
        c1, c2, c3 = float(input()), float(input()), float(input())
        suma = c1 + c2 + c3
        prom = suma / 3
        if prom >= 8 and prom >= 9.5:
            print(f"Bienvenid@ {nombre} fuiste acepatada en la Universidad, tu edad es {edad} y tu promedio es {prom:.2f}")
        else:
            print("Solo aceptamos calificaciones entre 8 y 9.5")
    
    else:
        print("Solo aceptamos mayores de 21 años ")
else:
    print("Solo acepatamos mujeres en la Universidad")


print("\nProceso terminado...")

