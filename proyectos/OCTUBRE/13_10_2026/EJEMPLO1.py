def limpiar(texto):
    texto = texto.replace("\n", " ")
    return texto.strip().lower()
def esta_vacio(texto):
    return limpiar(texto) == ""


entrada = " "
print(esta_vacio(entrada))