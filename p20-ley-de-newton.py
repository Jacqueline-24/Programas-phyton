# Calcula la segunda ley de newton ( f = m * a )

print("[f]uerza  f = m * a")
print("[M]asa  m = f / a")
print("[A]celeracion  a = f / m")
op = input("Elige ?").upper()

if op == "F":
    print("\nCalculando la Fuerza")
    m = float(input("Dame la Masa ?"))
    a = float(input("Dame la Aceleracion ?"))
    f = m * a
    print(f"\nLa Fuerza es {f:.2f}")
elif op == "M":
    print("\nCalculando la Masa")
    f = float(input("Dame la Fuerza ?"))
    a = float(input("Dame la Aceleracion ?"))
    m = f / a 
    print(f"\nLa Masa es {m:.2f}")
elif op == "A":
    print("\nCalculando la Aceleracion")
    f = float(input("Dame la Fuerza ?"))
    m = float(input("Dame la Masa ?"))
    a = f / m
    print(f"\nLa Aceleracion es {a:.2f}")
else:
    print("\nOpcion Invalida")

print("\nProceso terminado")