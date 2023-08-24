# Lee datos del usuario y envía un saludo la pantalla

print("Leyendo datos y enviando un mensaje a pantalla")

nombre = input("Dame tu nombre?")
edad   = int(input ("Dame la edad?"))
peso   = float(input("Dame el peso"))

print(f"\nTu nombre es {nombre} tu edad es {edad} tu peso es {peso}")

print(type(nombre))
print(type(edad))
print(type(peso))