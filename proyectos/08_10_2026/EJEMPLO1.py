def saludar(nombre):
    mensaje= "Hola, " + nombre + ", bienvenido"
    return mensaje

def primeramayuscula(nombre):
    nombre = nombre.strip()
    nombre = nombre[0].upper() + nombre[1:]
    return nombre
    

resultado = (input("Ingrese su nombre: "))
texto=saludar(primeramayuscula(resultado))
print(texto)