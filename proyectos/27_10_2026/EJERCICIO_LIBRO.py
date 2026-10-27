import json

mensajes = [
    {
    "role" : "Lista",
    "content" : "Esto es una lista" 
    },
    {
    "role" : "Diccionario",
    "content" : "Esto es un diccionario" 
    } 
]

with open("libro.json", "w", encoding ="utf-8") as archivo:
    json.dump(mensajes, archivo, ensure_ascii=False, indent=2) 

with open("libro.json", "r", encoding ="utf-8") as archivo:
    datos = json.load(archivo)

print(datos[-1]["content"])