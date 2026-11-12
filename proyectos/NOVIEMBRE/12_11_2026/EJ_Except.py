try:
    datos = cargar_configuracion("config.json")
except Exception as e:
    print(type(e).__module__, type(e).__name__)
    print(type(e).__mro__)