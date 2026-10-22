historial = ["Hola", "Explicame IA", "pruebas"]

with open("historial.txt", "w", encoding="utf=8") as archivo:
    for mensaje in historial:
        archivo.write(mensaje() + "\n")

with open("historial.txt", "r", encoding="utf=8") as archivo:
        print (archivo.readline)