#Se desea procesar el pedido de una pizza en base a sus ingredientes
import os
os.system("cls")

ingredientes = {"T": 1.50, "P": 3.50, "A": 0.40, "Q": 3.74, "I": 2.10}

pedido = input("Ingredientes de tu pizza ? ")
if not pedido :
    print("Precio base es de 15, compra de más de 20 descuento del 5%")
    for ingrediente, precio in ingredientes.items():
        print(f"{ingrediente} - {precio}")

else:
    subtotal = 15  

    for ingrediente in pedido:
        if ingrediente in ingredientes:
            subtotal += ingredientes[ingrediente]
        else:
            print("No seleccionaste ingredientes validos")
            exit()
           
    total = subtotal

    if subtotal > 30:
        descuento = subtotal * 0.05
        total -= descuento


    print(f"El subtotal  es : {subtotal}")
    print(f"El total es     : {total}")


