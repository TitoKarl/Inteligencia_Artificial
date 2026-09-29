etiqueta = input("Ingrese frase con guiones: ")
partes=etiqueta.split("-")

palabras=len(partes)
for valor in range(palabras):
    print(partes[valor])

