frase = input("Introduce una frase: ")

frase_limpia = frase.strip()
frase_min = frase_limpia.lower()
numero_caracteres = len(frase_limpia)

print("Frase: ", frase_limpia)
print("Minusculas: ", frase_min)
print("Numero: ", numero_caracteres)