import json

with open("historial.json", "r", encoding="utf-8") as archivo:
    mensajes = json.load(archivo)

buscar = input("Introduce el rol a buscar: ").strip()

for mensaje in mensajes:
    if mensaje["role"].lower() == buscar.lower():
        print(mensaje["content"])
else:
    print("No se encontró ningún mensaje con ese rol.")