# Dado un numero del 1 al 7 mostrar los dias de la semana correspondiente, 1 es domingo, 2 es lunes y así sucesivamente hasta 7 es viernes.

print("\nVerifica el dia de la semana")


dia = int(input("Dame un numero ?"))


if dia == 1:
    print(f"El dia {dia} es Domingo")
elif dia == 2:
        print(f"El dia {dia} es Lunes")
elif dia == 3:
        print(f"El dia {dia} Martes")
elif dia == 4:
        print(f"El dia {dia} es Miercoles")
elif dia == 5:
        print(f"El dia {dia} es Jueves")
elif dia == 6:
        print(f"El dia {dia} es Viernes")
elif dia == 7:
        print(f"El dia {dia} es Sabado")

else:
    print("El dia no existe")


print("\nProceso terminado")