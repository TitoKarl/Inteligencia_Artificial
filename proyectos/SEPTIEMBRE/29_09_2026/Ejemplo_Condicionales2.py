score = 0.86
contiene_datos = True
fuente_conocida = True

es_confiable = score > 0.8 and fuente_conocida
requiere_revision = not es_confiable or contiene_datos
print(es_confiable)
print(requiere_revision)