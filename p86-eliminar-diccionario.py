# Cree un diccionario de municipios
import os 
os.system("cls")

municipios = {
    "Apozol"   : 1863,
    "Calera"   : 1868,
    "Fresnillo": 1554,
    "Guadalupe": 1821,
    "Jalpa"    : 1824,
    "Jerez"    : 1824,
    "Loreto"   : 1931,
    "Mazapil"  : 1824,
    "Momax"    : 1857
}


print(f"\nDiccionario original: \n {municipios}")


del municipios["Apozol"]
print("\nDiccionario municipio Apozol eliminado :", municipios, len(municipios))
municipios.pop("Fresnillo")
print("\nDiccionario municipio Fresnillo eliminado:", municipios, len(municipios))
municipios.popitem()
("Momax", 1857)
print("\nDiccionario municipio Momax eliminado:", municipios, len(municipios))
municipios.clear()
print(f"\nDiccionario municipios eliminados : \n {municipios}")