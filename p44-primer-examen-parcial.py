# Imprima el control de la inscripción a un evento académico de la Universidad Patito. Se especifica: Tipo de usuario, paquete y cantidad.

import os

while(True):
    os.system("cls")
    print("Universidad patito SA. de CV")
    print("Sistema de Inscripción Congreso de Sistemas")

    subtotal = 0
    descuento = 0
    total = 0
    suma= 0
    alum = 100
    trabajador = 200
    docente = 500
    solconf = 600
    eventosocial = 800
    kitacceso = 900

    while suma <= 500000000000 : 
        tusuario = int(input("[1] Alumno $100, [2] Trabajador $200, [3] Docente $500 ?"))
        tpaquete = int(input("[1] Solo conferencias $600, [2] Con eventos sociales $800, [3] Con kit de acceso $900 ?"))
        cant = int(input("Cantidad ?"))

        if tusuario == 1 and tpaquete == 1 :
            tusuario = "Alumno"
            tpaquete = "Solo conferencia"
            subtotal = (alum + solconf)*cant
            if subtotal > 5000 :
               descuento = subtotal * 0.20
               total = subtotal-descuento

        if tusuario == 1 and tpaquete == 2:
            tusuario = "Alumno"
            tpaquete = "Solo conferencia"
            subtotal = (alum + eventosocial)*cant
            if subtotal > 5000 :
               descuento = subtotal * 0.20
               total = subtotal-descuento

        if tusuario == 1 and tpaquete == 3:
            tusuario = "Alumno"
            tpaquete = "Con kit de acceso"
            subtotal = (alum + kitacceso)*cant
            if subtotal > 5000:
               descuento = subtotal*0.20
               total = subtotal-descuento

        if tusuario == 2 and tpaquete==1:
            tusuario="Trabajador"
            tpaquete="Solo conferencias"
            subtotal = (trabajador+solconf)*cant
            if subtotal > 5000:
               descuento = subtotal*0.10
               total = subtotal-descuento

        if tusuario == 2 and tpaquete == 2:
            tusuario ="Trabajador"
            tpaquete = "Con evento social"
            subtotal = (trabajador+eventosocial)*cant
            if subtotal > 5000:
                descuento=subtotal*0.10
                total=subtotal-descuento

        if tusuario ==2 and tpaquete==3:
            tusuario="Trabajador"
            tpaquete="Con kit de acceso"
            subtotal=(trabajador+kitacceso)*cant
            if subtotal > 5000:
                descuento=subtotal*0.10
                total=subtotal-descuento

        if tusuario == 3 and tpaquete == 1:
            tusuario ="Docente"
            tpaquete ="Solo conferencias"
            subtotal=(docente+solconf)*cant
            if subtotal > 5000:
                descuento=subtotal*0.05
                total=subtotal-descuento

        if tusuario == 3 and tpaquete == 2:
            tusuario="Docente"
            tpaquete="Con evento social"
            subtotal=(docente+eventosocial)*cant
            if subtotal > 5000:
                descuento=subtotal*0.05
                total=subtotal-descuento

        if tusuario == 3 and tpaquete == 3:
            tusuario="Docente"
            tpaquete="Con kit de acceso"
            subtotal=(docente+kitacceso)*cant
            if subtotal > 5000:
                descuento=subtotal*0.05
                total=subtotal-descuento

        print(f"El pedido fue: {cant}, el tipo de usuario es : {tusuario} y el paquete es: {tpaquete}")
        print(f"El subtotal es: {subtotal}, con un descuento de: {descuento} y el total es: {total}")
        suma = suma+total
      
                

        resp = input("Deseas continuar (S/N)? ").upper()
        if resp== "N": 
            break

    print(f"El total de la venta es de: {suma}")
    print("\nProceso terminado...")
    break


                           

