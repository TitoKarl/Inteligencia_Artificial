datos_personales = True
confianza = float(input("Ingrese el nivel de confianza (0-1): "))

if datos_personales and confianza >= 0.7:
    print("Acceso concedido")
else:
    print("Acceso denegado")