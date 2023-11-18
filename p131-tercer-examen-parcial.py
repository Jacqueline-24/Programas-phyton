import os
os.system('cls')
class Jugador:
    def __init__(self, nombre, añonac, sexo, becado):
        self.nombre = nombre
        self.añonac = añonac
        self.sexo = sexo
        self.becado = becado

class Categoria:
    def __init__(self, nombre, rango, costo):
        self.nombre = nombre
        self.rango = rango
        self.costo = costo
        self.jugadores = []
    def agregarJugador(self, jugador):
        self.jugadores.append(jugador)
    def calcularSubtotal(self):
        subtotal = sum([jugador.becado == "Sin Beca" for jugador in self.jugadores]) * self.costo
        return subtotal

class Academia:
    def __init__(self, nombre, propietario, domicilio):
        self.nombre = nombre
        self.propietario = propietario
        self.domicilio = domicilio
        self.categorias = []
    def agregarCategoria(self, categoria):
        self.categorias.append(categoria)
    def calculartotalCategorias(self):
        return len(self.categorias)
    def calculartotalHombresMujeres(self):
        totalhombres = sum([sum([1 for jugador in categoria.jugadores if jugador.sexo == "Hombre"]) for categoria in self.categorias])
        totalmujeres = sum([sum([1 for jugador in categoria.jugadores if jugador.sexo == "Mujer"]) for categoria in self.categorias])
        return totalhombres, totalmujeres

    def imprimirReporte(self):
        print("Reporte del Club Deportivo")
        print(f"Nombre: {self.nombre}")
        print(f"Propietario: {self.propietario}")
        print(f"Domicilio: {self.domicilio}")
        print(f"Total de Categorias: {self.calculartotalCategorias()}")
        totalhombres, totalmujeres = self.calculartotalHombresMujeres()
        print(f"Total de Hombres: {totalhombres}")
        print(f"Total de Mujeres: {totalmujeres}")
        print("Datos generales de las Categorias")
        for categoria in self.categorias:
            print(f"Nombre: {categoria.nombre} Rango: {categoria.rango} Costo: ${categoria.costo:.2f}")
            print("Jugadores por Categoria:")
            print(f" {categoria.nombre} - {categoria.rango} - ({len(categoria.jugadores)})")
            for jugador in categoria.jugadores:
                print(f"Nombre: {jugador.nombre} AñoNac: {jugador.añonac} Sexo: {jugador.sexo} Becado: {jugador.becado}")
            subtotal = categoria.calcularSubtotal()
            print(f"- SubTotal : ${subtotal:.2f}\n")
        total_ingresos = sum([categoria.calcularSubtotal()
        for categoria in self.categorias])
        print(f"-> Total : ${total_ingresos:.2f}")

# Programa principal
jugador1 = Jugador("Alexander Lopez", 2006, "Hombre", "Sin Beca")
jugador2 = Jugador("Uriel Puga", 2007, "Hombre", "Becado")
jugador3 = Jugador("Alejandra Escalona", 2008, "Mujer", "Sin Beca")

jugador4 = Jugador("Armando Santana", 2009, "Hombre", "Sin Beca")
jugador5 = Jugador("Daniel Mijares", 2010, "Hombre", "Sin Beca")
jugador6 = Jugador("Antonio Hernandez", 2011, "Mujer", "Becado")

jugador7 = Jugador("Andrea Solis", 2012, "Mujer", "Becado")
jugador8 = Jugador("Marissa Hernandez", 2013, "Mujer", "Becado")
jugador9 = Jugador("Diana Soto", 2014, "Mujer", "Sin Beca")

categoria1 = Categoria("Junior A", "2006/2007/2008", 1250.00)
categoria1.agregarJugador(jugador1)
categoria1.agregarJugador(jugador2)
categoria1.agregarJugador(jugador3)

categoria2 = Categoria("Junior B", "2009/2010/2011", 850.00)
categoria2.agregarJugador(jugador4)
categoria2.agregarJugador(jugador5)
categoria2.agregarJugador(jugador6)

categoria3 = Categoria("Pony A", "2012/2013/2014", 700.00)
categoria3.agregarJugador(jugador7)
categoria3.agregarJugador(jugador8)
categoria3.agregarJugador(jugador9)

academia = Academia("Academia Santos Laguna", "Francisco Nava", "Aguanaval 123, Hidráulica")
academia.agregarCategoria(categoria1)
academia.agregarCategoria(categoria2)
academia.agregarCategoria(categoria3)

academia.imprimirReporte()