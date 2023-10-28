# Imprime el dia de la semana 

def semana(dia):
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    if dia < 1 or dia > 7:
        return "No existe" 
    exit
    return dias[dia - 1]

# Programa principal
num = int(input("Ingresa un número : "))
ndias = semana(num)
print(f"El día de la semana es: {ndias}")
