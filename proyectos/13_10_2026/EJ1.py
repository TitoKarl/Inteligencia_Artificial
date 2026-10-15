def pedir_texto():
    return input("Introduce un texto: ")

def limpiar(texto):
    return texto.strip().lower()

def mostrar_resultado(resultado):
    print("El resultado es: ", resultado)

def es_pregunta(texto):
    return texto[-1] == "?"

texto = pedir_texto()
texto_limpio = limpiar(texto)
print(texto_limpio)
print(es_pregunta(texto_limpio))
