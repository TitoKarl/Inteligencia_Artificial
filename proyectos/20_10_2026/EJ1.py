with open("notas.txt", "w", encoding="utf-8") as f:
    f.write("7\n")
    f.write("8\n")
    f.write("6\n")
with open("notas.txt", "r", encoding="utf-8") as f:
    for linea in f:
        print(linea.strip())