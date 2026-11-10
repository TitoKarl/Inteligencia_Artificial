import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
CARPETA = os.path.join(BASE, "apuntes")
RUTA_INDICE = os.path.join(BASE, "indice.json")

SIGNOS = ".,;:!?()[]{}\"'"


def normalizar(palabra):
    return palabra.strip().lower().strip(SIGNOS)


def leer_lineas(ruta):
    with open(ruta, encoding="utf-8") as archivo:
        return archivo.read().splitlines()


def archivos_txt():
    return sorted(
        nombre
        for nombre in os.listdir(CARPETA)
        if nombre.lower().endswith(".txt")
    )


def palabras_de(linea):
    palabras = []
    for trozo in linea.lower().split():
        palabra = trozo.strip(SIGNOS)
        if palabra:
            palabras.append(palabra)
    return palabras


def buscar(palabra):
    buscada = normalizar(palabra)
    resultados = []

    for nombre in archivos_txt():
        ruta = os.path.join(CARPETA, nombre)
        for numero, linea in enumerate(leer_lineas(ruta), start=1):
            if buscada in palabras_de(linea):
                resultados.append((nombre, numero))
                print(f"{nombre}, línea {numero}")

    if not resultados:
        print("No aparece")

    return resultados


def crear_indice():
    indice = {}

    for nombre in archivos_txt():
        ruta = os.path.join(CARPETA, nombre)
        for numero, linea in enumerate(leer_lineas(ruta), start=1):
            for palabra in palabras_de(linea):
                lugares = indice.setdefault(palabra, [])
                lugar = [nombre, numero]
                if lugar not in lugares:
                    lugares.append(lugar)

    lineas = [
        f"  {json.dumps(palabra, ensure_ascii=False)}: {json.dumps(lugares, ensure_ascii=False)}"
        for palabra, lugares in sorted(indice.items())
    ]
    with open(RUTA_INDICE, "w", encoding="utf-8") as archivo:
        archivo.write("{\n" + ",\n".join(lineas) + "\n}\n")

    return indice


def cargar_indice():
    if not os.path.exists(RUTA_INDICE):
        print("No hay indice todavia; creandolo...")
        return crear_indice()

    with open(RUTA_INDICE, encoding="utf-8") as archivo:
        return json.load(archivo)


def main():
    indice = cargar_indice()
    print("Buscador de apuntes. Escribe 'salir' para terminar.")

    while True:
        palabra = input("Palabra: ")

        if normalizar(palabra) == "salir":
            break
        if not palabra.strip():
            continue

        lugares = indice.get(normalizar(palabra), [])
        if lugares:
            for nombre, numero in lugares:
                print(f"{nombre}, línea {numero}")
        else:
            print("No aparece")

    print("El programa ha terminado")


if __name__ == "__main__":
    main()
