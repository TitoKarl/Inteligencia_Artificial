import json

try:
    with open("config.json", "r") as archivo:
        datos = json.load(archivo)
except Exception as e:
    print(type(e).__module__, type(e).__name__)
    print(type(e).__mro__)