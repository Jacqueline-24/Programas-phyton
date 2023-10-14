# Cree un diccionario de llave numérica dias
import os
os.system("cls")

dias = {
    1: "Lunes",
    2: "Martes",
    3: "Miércoles",
    4: "Jueves",
    5: "Viernes",
    6: "Sábado",
    7: "Domingo"
}

print("\nSe muestra en un diccionario los dias de la semana")

primerelemento = dias[1]
ultimoelemento = dias[7]

print("El primer elemento es :", primerelemento)
print("El ultimo elemento es :", ultimoelemento)

quintodia = dias.get(5)
print("El quinto dia es:", quintodia)

septimodia = dias.get(7)
print("El septimo dia es:", septimodia)

print(f"\nDiccionario completo : \n {dias}")