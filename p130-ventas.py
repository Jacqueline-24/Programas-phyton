import os
class Venta:
    def __init__(self, articulo, cantidad, precio):
        self.articulo = articulo
        self.cantidad = cantidad
        self.precio = precio
        self.total = cantidad*precio
    def __str__(self):
            return f"Articulo:{self.articulo:<5}, Cantidad:{self.cantidad:>5.2f}, Precio:{self.precio:>5,.2f}, Total:{self.total:>10,.2f}"

class Cliente:
    def __init__(self,rfc,nombre,domicilio,correo):
        self.rfc=rfc
        self.nombre=nombre
        self.domicilio=domicilio
        self.correo=correo
        self.ventas=list()
    def agregarVenta(self, venta):
        self.ventas.append(venta)
    def totalVentas(self):
        total=0
        for venta in self.ventas:
            total+= venta.total
        return total
    def __str__(self):
        return f"Cliente -> [Nombre:{self.nombre:<5}, RFC:{self.rfc:<5}, Domicilio: {self.domicilio:<5}, Correo: {self.correo:<20}]"
    
class Tienda:
    def __init__(self,nombre,domicilio,propietario):
        self.nombre=nombre
        self.domicilio=domicilio
        self.propietario=propietario
        self.clientes=list()
    def agregarCliente(self, cliente):
        self.clientes.append(cliente)
    def totalVentas(self):
        total=0
        for cliente in self.clientes:
            total += len(cliente.ventas)
        return total
    def totalImporteVentas(self):
        total=0
        for cliente in self.clientes:
            total+= cliente.totalVentas()
        return total
    def __str__(self):
        return f"Tienda -> [Nombre: {self.nombre} Domicilio: {self.domicilio}, Propietario: {self.propietario}]"
    
def main():
    os.system("cls")
    print("Inicio del programa principal en la funcion main()\n")
    mitienda = Tienda(nombre="Ferreteria las Lomas", domicilio="Av Luis Moya 345", propietario=" Carlos Castaneda")
    mitienda.agregarCliente(Cliente(rfc="JELI120240", nombre="Felipe Calderon", domicilio="Las Lomas 123", correo="cald@.com"))
    mitienda.agregarCliente(Cliente(rfc="PEÑA121250", nombre="Enrique Peña", domicilio="5 de Mayo 321", correo="quique@gmail.com"))
    mitienda.agregarCliente(Cliente(rfc="AMLO101145", nombre="Andres Lopez", domicilio="Palacio Nacional 123", correo="cald@.com"))
    mitienda.agregarCliente(Cliente(rfc="GELA666666", nombre="Xochitl Gelatinas", domicilio="Danone 123", correo="xochitl@residencia.gob.mx"))
    mitienda.clientes[0].agregarVenta(Venta(articulo="Martillo",cantidad=10, precio=60.5))
    mitienda.clientes[0].agregarVenta(Venta(articulo="Pala",cantidad=2, precio=1170.55))
    mitienda.clientes[1].agregarVenta(Venta(articulo="Clavo",cantidad=2.5, precio=160.34))
    mitienda.clientes[1].agregarVenta(Venta(articulo="Cinta de aislar",cantidad=5, precio=71.34))
    mitienda.clientes[2].agregarVenta(Venta(articulo="Tiner",cantidad=50, precio=65.00))
    mitienda.clientes[3].agregarVenta(Venta(articulo="Pinzas de Chofer",cantidad=1, precio=300.00))

    # Reporte
    print(f"Reporte de ventas: {mitienda}")
    print(f"total de clientes: {len(mitienda.clientes)}")
    print(f"Total de ventas  : {mitienda.totalVentas()}")
    print("\nClientes")
    for cliente in mitienda.clientes:
        print(cliente)
    for cliente in mitienda.clientes:
        print(f"\n{cliente.rfc} - {cliente.nombre} - {cliente.totalVentas():,.2f}")
        print()
        for venta in cliente.ventas:
            print(f"- {venta}")
    print(f"\nTotal importe ventas : {mitienda.totalImporteVentas():,.2f}")

if __name__ == "__main__": 
    main()