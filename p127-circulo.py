import math 

class Circulo:
    def __init__(self, radio):
        self.radio = radio 
    def obtenerArea(self):
        return math.pi * math.pow(self.radio,2)
    def obtenerCircunferencia(self):
        return 2 * math.pi * self.radio
    def __str__(self):
        return f"Radio = {self.radio:.2f}, Area = {self.obtenerArea():.2f}, Circunferencia = {self.obtenerCircunferencia():.2f}"
    
circulo1 = Circulo(10.40)
print(circulo1)
print(f"El radio: {circulo1.radio:.2f}")
print(f"El area: {circulo1.obtenerArea():.2f}")
print(f"La circu: {circulo1.obtenerCircunferencia():.2f}")
circulo2 = Circulo(12.45)
print(circulo2)
print(f"El radio: {circulo2.radio:.2f}")
print(f"El area: {circulo2.obtenerArea():.2f}")
print(f"La circu: {circulo2.obtenerCircunferencia():.2f}")
circulo3 = Circulo(100)
print(circulo3)
print(f"El radio: {circulo3.radio:.2f}")
print(f"El area: {circulo3.obtenerArea():.2f}")
print(f"La circu: {circulo3.obtenerCircunferencia():.2f}")

areatotal = circulo1.obtenerArea() + circulo2.obtenerArea() + circulo3.obtenerArea();
print(f"El area total de los circulos es {areatotal:.2f}")



    