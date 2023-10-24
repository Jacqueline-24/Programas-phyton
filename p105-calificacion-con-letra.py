# Regresa una letra y un mensaje de acuerdo al promedio

def califletra(prom):
    letra = ""
    msj = ""
    if prom>=90 and prom<=100:
        letra = "A"; msj ="Excelente"
    elif prom>=80 and prom<=90:
        letra ="B"; msj = "Bien"
    elif prom>=70 and prom<=80:
        letra = "C"; msj ="Suficiente"
    elif prom>=60 and prom<=70:
        letra = "D"; msj ="Deficiente"
    elif prom>=0 and prom<=60:
        letra = "F"; msj = "Reprobado"
    return letra, msj

# Programa principal
prom = int(input("Dame tu promedio entre 1 y 100 ?"))
letra, msj = califletra(prom)

print(f"Tu promedio es de {prom} corresponde a la letra {letra} y es {msj}")
