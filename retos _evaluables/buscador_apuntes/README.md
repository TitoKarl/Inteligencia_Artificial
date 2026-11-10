# Reto evaluable: buscador en tus apuntes

Programa que busca una palabra en los archivos `.txt` de la carpeta `apuntes` y
dice en que archivo y en que linea aparece.

## Estructura

```text
buscador_apuntes/
|-- apuntes/
|   |-- soporte.txt
|   |-- tema3.txt
|   `-- tema4.txt
|-- buscador.py
|-- indice.json
`-- README.md
```

## Como ejecutarlo

Desde la carpeta `buscador_apuntes`:

```text
python buscador.py
```

El programa carga `indice.json` y pide palabras hasta que se escriba `salir`.

Para probar las funciones por separado:

```text
python -c "import buscador; print(buscador.leer_lineas('apuntes/soporte.txt'))"

python -c "import buscador; buscador.buscar('json')"

python -c "import buscador; buscador.crear_indice(); print('Indice creado')"
```

Si se modifican los archivos de `apuntes`, hay que volver a ejecutar
`crear_indice()` para actualizar `indice.json`.

## Explicacion de las cuatro partes

### Parte 1. `leer_lineas(ruta)`

```python
with open(ruta, encoding="utf-8") as archivo:
    return archivo.read().splitlines()
```

- `open(..., encoding="utf-8")` abre el archivo con la codificacion correcta.
- `read()` devuelve todo el contenido en un solo texto.
- `splitlines()` parte ese texto en lineas y elimina el salto de linea final
  (`\n`). Asi cada elemento de la lista es la linea limpia.
- El `with` cierra el archivo automaticamente al terminar.

Resultado:

```text
leer_lineas("apuntes/soporte.txt")
-> ["Si el equipo no enciende, revisa el cable.",
    "Si no hay conexion, reinicia el router."]
```

### Parte 2. `buscar(palabra)`

```python
for nombre in archivos_txt():
    for numero, linea in enumerate(leer_lineas(ruta), start=1):
        if buscada in palabras_de(linea):
```

- `os.listdir(CARPETA)` devuelve los nombres de los archivos de la carpeta sin
  necesidad de conocerlos de antemano.
- `nombre.lower().endswith(".txt")` se queda solo con los `.txt`, sin importar
  si la extension esta escrita en mayusculas.
- `enumerate(..., start=1)` lleva la cuenta de la linea empezando en 1, como
  cuentan las personas.
- `normalizar()` pasa la palabra buscada a minusculas, y `palabras_de()` hace lo
  mismo con cada palabra del archivo. Por eso `JSON` y `json` son la misma
  palabra.
- `palabras_de()` tambien quita comas, puntos y otros signos de los extremos:
  `"enciende,"` se guarda como `"enciende"`.

Resultado:

```text
buscar("json")
-> tema3.txt, linea 2
-> tema4.txt, linea 2
```

### Parte 3. `crear_indice()`

El indice es un diccionario que asocia cada palabra con una lista de lugares:

```json
{
  "json": [["tema3.txt", 2], ["tema4.txt", 2]],
  "cable": [["soporte.txt", 1]]
}
```

- Se recorre cada archivo y cada linea con `enumerate(..., start=1)`.
- `palabras_de(linea)` parte la linea en palabras y limpia los signos.
- `indice.setdefault(palabra, [])` resuelve el caso de la primera aparicion:
  si la palabra no esta todavia en el diccionario, crea una lista vacia; si ya
  esta, devuelve la lista que ya existia. Despues se anade el lugar con
  `.append([nombre, numero])`.
- Se comprueba `if lugar not in lugares` para no guardar dos veces la misma
  palabra en la misma linea.
- `json.dump(..., ensure_ascii=False, indent=2)` guarda el diccionario en
  `indice.json` con formato.

### Parte 4. `main()`

```python
resultados = indice.get(normalizar(palabra), [])
```

- `input()` lee la palabra escrita por el usuario.
- El bucle `while True` termina cuando se escribe `salir`.
- `indice.get(clave, [])` evita el `KeyError`: si la palabra no existe en el
  indice, devuelve una lista vacia en lugar de dar un error. No hace falta
  usar `try`.
- Si la lista tiene elementos, se muestra cada `archivo, linea N`; si esta
  vacia, se muestra `No aparece`.

## Respuesta a la pregunta de reflexion

Buscamos `enciende` y luego `arranca`:

```text
Palabra: enciende
soporte.txt, linea 1
Palabra: arranca
No aparece
```

Porque el buscador compara palabras literales y en `soporte.txt` esta escrito
`no enciende`: la palabra `arranca` no aparece en ningun archivo.
El indice no guarda sinonimos ni significados; para encontrarla habria que
escribir `arranca` en los apuntes o anadir esa equivalencia al buscador.

## Decisiones de diseno

- Se busca la palabra completa, no un trozo: `json` no coincidiria con
  `jsonl`. Esto evita resultados falsos y encaja con la idea de "palabra".
- La busqueda no distingue mayusculas de minusculas (`JSON` = `json`), pero si
  distingue las letras con tilde.
- Las rutas se construyen a partir de la ubicacion de `buscador.py`, asi el
  programa funciona aunque se ejecute desde otra carpeta.
