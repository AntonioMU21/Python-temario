lista = [10, 3, 25, 8, 15, 7, 40, 11, 9, 30]

lista2 = []

for i in range(len(lista)):
    if lista[i] % 5 == 0:
        lista2.append(lista[i])

with open("multiplos.txt", "w", encoding="utf-8") as f:
    for i in range(len(lista2)):
        linea = str(lista2[i]) + "\n"
        f.write(linea)

print("Fichero generado")
