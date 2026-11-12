def pedir_temperatura(texto):
    """Convierte el texto en un numero entre 0 y 2."""
    valor = float(texto)
    if not () <= valor <= 2:
        raise ValueError("La temperatura debe estar entre 0 y 2.")
    return valor

try:
    t = pedir_temperatura(input("Temperatura: "))
except ValueError as e:
    print("Dato no valido: ", e)