class Empleado:
    def __init__(self, nombre, edad, sexo, casado):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.casado = casado
    def __str__(self):
        return f'Nombre: {self.nombre}, Edad: {self.edad}, Sexo: {"Mujer" if self.sexo=="M" else "Hombre"}, Casado: {"Casado"  if self.casado else "No casado"}'
    
# Programa principal
emp1 = Empleado("Jose Díaz", 35, "H", True)
print("Nombre: ", emp1.nombre)
print("Edad:   ", emp1.edad)
print("Sexo: ", emp1.sexo)
print("Casado: ", emp1.casado)
print(emp1)

emp2 = Empleado("Maria Lopez", 22, "M", False)
print(emp2)

emp3 = Empleado("Rosario Valenzuela", 15, "M", True)
print(emp3)
emp4 = Empleado("Juan Perez", 20, "H", False)
prom = (emp1.edad + emp2.edad + emp3.edad + emp4.edad) /4
print("Promedio de edades de los empleados: ", prom)
print(f"Los nombres son : {emp1.nombre}, {emp2.nombre}, {emp3.nombre}, {emp4.nombre}")
if(emp2.casado==False and emp4.casado==False):
    print(f"\n{emp2.nombre} se puede casar con {emp4.nombre} ambos son solteros")
if(emp1.casado==True and emp3.casado==True):
    print(f"\n{emp1.nombre} no se puede casar con {emp3.nombre} por que estan casados")

