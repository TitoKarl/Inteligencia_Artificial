try:
    with open ("config.json", "r", encoding="utf-8") as f:
        config = json.load(f)
    print(contenido)
except FileNotFoundError:
    print("El archivo de configuración no se encontró.")
