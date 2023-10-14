# Cree un diccionario de países
import os  
os.system("cls")

print("\nSe muestra un diccionario con distintos paises")

paises = {
    'Argentina' : 100, 
    'Brasil'    : 200,
    'Colombia'  : 300, 
    'Chile'     : 400,
    'Ecuador'   : 500, 
    'Bolivia'   : 600, 
    'Jamaica'   : 700
    }
print(f"\nDiccionario original {paises}:")

paises['Brasil'] = 250
paises['Chile'] = 450
paises.update({'Bolivia': 650})
paises.update({'Jamaica': 750})
print(f"\nDiccionario actualizado : \n {paises}")
