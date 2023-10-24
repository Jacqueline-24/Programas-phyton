# Suma los digitos de un numero entero 1971 = 18

def sumadigito(n):
    suma = 0
    while n!=0:
        dig = n % 10
        suma = suma + dig
        n = n // 10
    return suma

# Programa principal
año =int(input("Dame tu año de nacimiento y te dire tu numero de la suerte ?"))
suerte = sumadigito(año)
print(f"Tu año de nacimiento es {año} por lo tanto tu numero de la suerte es {sumadigito(año)}")