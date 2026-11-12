import json

try:
    with open("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Falta config.json.")
except PermissionError:
    print("No tengo permiso para leer config.json.")
except json.JSONDecodeError:
    print("config.json no es un archivo JSON válido.")
else:
    print("Configuracion cargada: ", config)
finally:
    print("Fin de la garga.")