# Convierta: pulgadas a centímetros y metros a pies

def centimetros(pulgadas):
    return pulgadas * 2.54

def pies(metros):
    return metros * 3.281

# Programa principal
op = int(input("Elige ?"))
if op == 1:
    pulgadas = float(input("Ingresa el valor en pulgadas: "))
    print(f"Son {centimetros(pulgadas):.2f} centimetros")
elif op == 2:
    metros = float(input("Ingresa el valor en metros: "))
    print(f"Son {pies(metros):.2f} pies")
else:
    print("Opción incorrecta")