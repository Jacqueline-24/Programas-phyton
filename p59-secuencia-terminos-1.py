# Imprima la secuencia de términos armónicos el numero de renglones que el usuario desee y su suma
import os
os.system("cls")



num = int(input("Dame un numero ?"))
sum = 0

for i in range(1, num + 1):
    if i == 1:
        print("1 + ",end=" ")
        sum += 1
    elif i == num:
        print(f"1/{i}!",end=" ")
        sum += (1 / i)
    else:
        print(f"1/{i}!", end =" + ")
        sum += (1/i)
print(f'\nSuma: {sum}')


