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
                print(f"{nombre}, linea {numero}")

    if not resultados:
        print("No aparece")

    return resultados


def bloque(nombre, pares):
    """Devuelve un objeto JSON con una clave por linea y los valores en una sola linea."""
    lineas = [
        f"    {json.dumps(clave, ensure_ascii=False)}: {json.dumps(valor, ensure_ascii=False)}"
        for clave, valor in pares
    ]

    if not lineas:
        return f'  "{nombre}": {{}}'

    return f'  "{nombre}": {{\n' + ",\n".join(lineas) + "\n  }"


def escribir_indice(documento):
    texto = (
        "{\n"
        + ",\n".join(
            [
                bloque("archivos", documento["archivos"].items()),
                bloque("indice", sorted(documento["indice"].items())),
            ]
        )
        + "\n}\n"
    )

    with open(RUTA_INDICE, "w", encoding="utf-8") as archivo:
        archivo.write(texto)


def crear_indice():
    ids_archivos = {
        f"hola{numero}": nombre
        for numero, nombre in enumerate(archivos_txt(), start=1)
    }

    indice = {}

    for id_archivo, nombre in ids_archivos.items():
        ruta = os.path.join(CARPETA, nombre)
        for numero, linea in enumerate(leer_lineas(ruta), start=1):
            for palabra in palabras_de(linea):
                lugares = indice.setdefault(palabra, [])
                lugar = f"{id_archivo}.{numero}"
                if lugar not in lugares:
                    lugares.append(lugar)

    documento = {"archivos": ids_archivos, "indice": indice}
    escribir_indice(documento)

    return documento


def resolver_lugar(documento, lugar):
    id_archivo, numero = lugar.rsplit(".", 1)
    return documento["archivos"][id_archivo], int(numero)


def cargar_indice():
    if not os.path.exists(RUTA_INDICE):
        print("No hay indice todavia; creandolo...")
        return crear_indice()

    with open(RUTA_INDICE, encoding="utf-8") as archivo:
        return json.load(archivo)


def main():
    documento = cargar_indice()
    print("Buscador de apuntes. Escribe 'salir' para terminar.")

    while True:
        palabra = input("Palabra: ")

        if normalizar(palabra) == "salir":
            break
        if not palabra.strip():
            continue

        lugares = documento["indice"].get(normalizar(palabra), [])
        if lugares:
            for lugar in lugares:
                nombre, numero = resolver_lugar(documento, lugar)
                print(f"{nombre}, linea {numero}")
        else:
            print("Error")

    print("El programa ha terminado")


if __name__ == "__main__":
    main()
