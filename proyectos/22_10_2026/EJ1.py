import json

mensajes = [
    {
        "role": "user",
        "content": "Hola,como ests"
    },
    {
        "role": "asistente",
        "content": "Bien"
    }
]

with open("historial.json", "w", encoding="utf-8") as archivo:
    json.dump(mensajes, archivo, ensure_ascii=False, indent=2)

with open("historial.json", "r", encoding="utf-8") as archivo:
    historial = json.load(archivo)

    
