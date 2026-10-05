activo = True
rol = "usuario"

if activo and (rol == "admin" or rol == "Profesor"):
    print("Acceso concedido")
else:
    print("Acceso denegado")
    