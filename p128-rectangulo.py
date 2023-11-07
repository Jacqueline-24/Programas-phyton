class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho
    def obtenerArea(self):
        return self.largo * self.ancho
    def obtenerPerimetro(self):
        return 2 * self.largo + 2 * self.ancho
    def __str__(self):
        return f"Largo: {self.largo}, Ancho: {self.ancho}, Area={self.obtenerArea():.2f}, Perimetro= {self.obtenerPerimetro():.2f}"
    
r1 = Rectangulo(12,3.4)
print(r1)
print(f"Largo = {r1.largo}, Ancho= {r1.ancho}")
print(f"El area = {r1.obtenerArea():.2f}")
print(f"El perimetro = {r1.obtenerPerimetro():.2f}")

r2= Rectangulo(5.6, 7.8)
print(f"Largo = {r2.largo}, Ancho= {r2.ancho}")
print(f"El area = {r2.obtenerArea():.2f}")
print(f"El perimetro = {r2.obtenerPerimetro():.2f}")

rectangulos =[]
rectangulos.append(r1)
rectangulos.append(r2)

print(rectangulos)


    
    