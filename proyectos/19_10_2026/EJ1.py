lista = [
    {
    "nombre": "Carlos",
    "edad": 21,
    "numero": "121212121",
    },
    {
    "nombre": "Juan",
    "edad": 22,
    "numero": "121212121",
    },
    {
    "nombre": "Manolo",
    "edad": 23,
    "numero": "121212121",
    },
]

edad = int(input("Ingrese la edad: "))
value=0
for datos in lista:
    if (edad==datos["edad"]):
        print(datos["nombre"], datos["numero"])
    else:
        value+=1
if value!=0:
        print("No se encontro la edad")
    
    
