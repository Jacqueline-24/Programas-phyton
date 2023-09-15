# Pida un número entre 1 y 10 y muestre su equivalente en número romano ( I, II, III, IV, V,VI, VII, VIII, IX, X)

print("Muestrame un numero del 1 al 10 y dame su equivalente a numero romano")

num =int(input("Dame un numero ?"))


if num == 1:
      print(f"El numero {num} es equivalente al numero romano I")
elif num == 2:
     print(f"El numero {num} es equivalente al numero romano II")
elif num == 3:
      print(f"El numero {num} es equivalente al numero romano III")
elif num == 4:
      print(f"El numero {num} es equivalente al numero romano IV")
elif num == 5:
      print(f"El numero {num} es equivalente al numero romano V")
elif num == 6:
      print(f"El numero {num} es equivalente al numero romano VI")
elif num == 7:
      print(f"El numero {num} es equivalente al numero romano VII")
elif num == 8:
      print(f"El numero {num} es equivalente al numero romano VIII")
elif num == 9:
      print(f"El numero {num} es equivalente al numero romano IX")
elif num == 10:
      print(f"El numero {num} es equivalente al numero romano X")


else:
    print("El numero no se encuentra")