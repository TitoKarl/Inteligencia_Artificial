calificacion = float(input("Ingrese la calificación: "))
if calificacion < 0.5:
    print("Revisar")
elif calificacion < 0.8:  
    print("Dudoso")
else:
    print("Aceptar")