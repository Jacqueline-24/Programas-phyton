# Nos permite ejemplificar las operaciones basicas sobre conjuntos 
import os ; os.system("cls")
muns = {"Zacatecas", "Guadalupe", " Jerez", "Fresnillo"}

print (muns, len(muns), type (muns))

for mun in muns :
    print(mun, end =" ")

muns.add("Teul")
print("\n", muns, len(muns))

muns.update({"Luis Moya", "Ojocaliente", "Tepetongo"})
print(muns, len(muns))

muns.remove("Zacatecas")
print(muns, len(muns))

muns.discard("Cañitas")
muns.discard("Ojocaliente")
print(muns, len(muns))

if("Luis Moya" in muns): 
    print("Si esta") 
else: 
    print("No esta")

print( muns.pop() )
print(muns, len(muns))

muns.clear()
print(muns, len(muns))
