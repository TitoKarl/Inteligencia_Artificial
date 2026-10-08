def saludar(nombre):
    nombre = nombre.strip()
    nombre = nombre[0].upper() + nombre[1:]
    mensaje= "Hola, " + nombre + ", bienvenido"
    return mensaje

resultado = saludar(input("Ingrese su nombre: "))
print(resultado)