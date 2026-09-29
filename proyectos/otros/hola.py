print("Hola, mundo!")

nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola, {nombre}! Bienvenido a Python.")

print( "Hola, IA")
tema = "Inteligencia Artificial"
print ("Este curso utilizara Python para:", tema)


# Práctica 1
# ESCRIBE UN PROGRAMA QUE MUESTRE TRES USOS DE PYTHON RELACIONADOS CON IA, UNO POR LÍNEA:

print ("1. Procesamiento de lenguaje natural (NLP) para análisis de sentimientos.")
print ("2. Aprendizaje automático (Machine Learning) para predicciones y clasificación de datos.")
print ("3. Visión por computadora (Computer Vision) para reconocimiento de imágenes y objetos.")

# Práctica 2
# MODIFICA EL PROGRAMA PARA ALMACENAR ESOS TRES USOS EN VARIABLES Y MOSTRARLOS DENTRO DE UNA FASE:

uso1 = "Procesamiento de lenguaje natural (NLP) para análisis de sentimientos."
uso2 = "Aprendizaje automático (Machine Learning) para predicciones y clasificación de datos."
uso3 = "Visión por computadora (Computer Vision) para reconocimiento de imágenes y objetos."
print ("Los tres usos de Python relacionados con IA son:" + uso1 + ", " + uso2 + " y " + uso3)
#Otra forma de hacerlo sin tantas comillas es utilizando f-strings:
print (f"Los tres usos de Python relacionados con IA son: {uso1}, {uso2} y {uso3}.")


# EJEMPLO:
edad = 18
precio = 12,50
curso = "DAM"
activo = True

print(type(edad))
print(type(precio))
print(type(curso))
print(type(activo))

# PRÁCTICA 3
# CREA VARIABLES PARA ALMACENAR: NÚMERO DE INCIDENCIAS, TIEMPO MEDIO DE RESOLUCIÓN, CATEGORÍA Y SI LA INCIDENCIA ESTÁ CERRADA. MUESTRA EL VALOR Y TIPO:

numero_incidencias = 5
tiempo_medio_resolucion = 2.5
categoria = "Tecnología"
esta_cerrada = False
for valor in [numero_incidencias, tiempo_medio_resolucion, categoria, esta_cerrada]:
    print(f"Valor: {valor}, Tipo: {type(valor)}")

# PRÁCTICA 4
# CORRIGE ESTE CÓDIGO PARA QUE CALCULE CORRECTAMENTE EL TOTAL: 'PRECIO 19,95, UNIDADES = 3; TOTAL = PRECIO * UNIDADES':

precio = 19.95
unidades = 3
total = float(precio) * unidades
print(f"Total: {total}")

# EJEMPLO

nombre = "Mateo"
horas = float (input("Horas de estudio: "))
días = int (input("Número de días: "))

media = horas / días
print (f"Hola {nombre}, tu media de horas de estudio por día es: {media:.2f} horas.")

# PRÁCTICA 5
# PIDE AL USUARIO MINUTOS EMPLEADOS EN UNA TAREA Y CONVIERTE EL RESULTADO A HORAS:

minutos = float(input("Introduce los minutos empleados en la tarea: "))
horas = minutos / 60
print(f"El tiempo usado en horas es: {horas:} horas.")

# PRÁCTICA 6
# PIDE NOMBRE, MÓDULO Y NOTA NUMÉRICA. MUESTRA UNA FRASE COMPLETA CON ESOS DATOS:

nombre = input("Introduce tu nombre: ")
modulo = input("Introduce el módulo: ")
nota = float(input("Introduce la nota numérica: "))
print(f"{nombre} ha obtenido una nota de {nota} en el módulo de {modulo}.")

# SACAR LA TABLA DE MULTIPLICAR DEL 9:

for i in range(1, 11):
    resultado = 9 * i
    print(f"9 x {i} = {resultado}") 

tokens_entrada = 1200
tokensa_salida = 300
total_tokens = tokens_entrada + tokensa_salida
porcentaje_salida = (tokensa_salida / total_tokens) * 100
print("Total:", total)
print("Porcentaje de tokens de salida:", porcentaje_salida, "%")


#P RÁCTICA 7
# CALCULA EL PRECIO FINAL DE UN SERVICIO CON PRECIO BASE, NÚMERO DE USOS Y DESCUENTO DLE 10%:

precio_base = float(input("Introduce el precio base del servicio: "))
numero_usos = int(input("Introduce el número de usos: "))

preciofinal = precio_base * numero_usos * 0.90

print(f"El precio final del servicio es: {preciofinal:.2f} €")

# Práctica 8
# DADO UN NÚMERO DE REGISTROS, CALCULA CUÁNTOS LOTES COMPLETOS DE 32 SE PUEDE FORMAR Y CUÁNTOS REGISTROS SOBRAN:

numero_registros = int(input("Introduce el número de registros: "))
lotes_completos = numero_registros // 32
registros_sobrantes = numero_registros % 32

print(f"Lotes completos de 32: {lotes_completos}")
print(f"Registros sobrantes: {registros_sobrantes}")

mensaje = "Error de CONEXIÓN"
limpio = mensaje.strip().lower() #Guarda el mensaje limpiando los espacios y pone las letras en minúsculas.
palabras = limpio.split() # Split divide las palabras de manera independiente.kf

print(limpio)
print(palabras)
print(f"El mensaje contiene {len(palabras)} palabras.")

# CONTAR LAS PALABRAS QUE TIENE UNA FRASE:

# 1. Pedimos la frase al usuario
frase = input("Introduce una frase: ")

# 2. Dividimos la frase en palabras independientes
palabras = frase.split()

# 3. Contamos cuántas palabras hay en la lista
numero_palabras = len(palabras)

# 4. Mostramos el resultado
print(f"La frase contiene {numero_palabras} palabras.").       # STRIP: ELIMINA ESPACIOS AL PRINCIPIO Y AL FINAL