num = float(input("Ingrese un valor entre 0 y 1: "))

while num < 0 or num > 1:
    num = float(input("Ingrese un valor entre 0 y 1: "))
    print("Numero ingresado:", num)