def pedir_texto(texto):
    texto = input("Introduce un texto: ")
    return texto.strip().lower()
def limpiar(texto):
    return texto.strip().lower()
def mostrar_resultado(resultado):
    print("El resultado es: ", resultado)

texto = pedir_texto("Introduce un texto: ")
texto_limpio = limpiar(texto)
print(texto_limpio)

