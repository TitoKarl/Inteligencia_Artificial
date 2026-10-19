# Crea una lista con tres diccionarios de mensaje: system, user y assistant.
# Despues recorrela e imprime role y content de cada uno

diccionario = [
    {"role": "System", 
     "content": "Soy un sistema."},

    {"role": "User", "content": 
     "Soy un usuario"},

    {"role": "Assistant", 
     "content": "Soy un asistente."}
]

for mensaje in diccionario:
    print(mensaje["role"])
    print(mensaje["content"])
    



