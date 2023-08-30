# Calcula la paga de un trabajador, las horas extras se pagan al doble

print("Calcula la paga de un trabajador, las horas extras se pagan al doble\n")

nombre = input( "Nombre ?")
horas = int (input("Horas trabajadas ?"))
paga = float(input("Paga x hora ?"))

extra = 0
if horas > 40 : 
    extra = horas - 40
    total = (40 * paga) + (2 * paga * extra)
else:
    total = horas * paga 

print(f"{nombre} trabajo {horas} horas, con paga de {paga }, hora extra {extra}, dando un total de {total:.2f}")
