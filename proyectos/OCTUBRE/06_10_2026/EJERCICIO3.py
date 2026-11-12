def primera_palabra(texto):
    palabras = texto.split()
    if palabras:
        return palabras[0]
    else:
        return ""

frase = "Python aplicado a IA"
primera = primera_palabra(frase)
print(primera)