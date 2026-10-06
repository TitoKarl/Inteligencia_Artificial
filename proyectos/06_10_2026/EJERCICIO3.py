def contar_palabras(texto):
    limpio = texto.strip()
    return len(limpio.split())

frase = "Python aplicado a IA"
cantidad = contar_palabras(frase)
print(cantidad)