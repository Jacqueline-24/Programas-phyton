# Convierta de grados centigrados a farenheit y veceversa

def farenheit(temp):
    return (temp * 9/5 ) + 32

def centigrados(temp):
    return (temp-32) * (5/9)

# Programa principal 
print("[ F ] arenheit")
print("[ C ] entigrados")
op = input("Elige ? ").upper()
if op=="F":
    temp = int(input("Dame centigrados ?"))
    print(f"Los farenheit son {farenheit(temp)}")
elif op=="C":
    temp = int(input("Dame farenheit ?"))
    print(f"Los centigrados son {centigrados(temp)}")
else:
    print("Opcion incorrecta")


