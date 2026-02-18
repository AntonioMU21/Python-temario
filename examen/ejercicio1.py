# Definimos la lista de 10 componentes (estilo Ejercicio-2 de clase)
lista = [10, 3, 15, 22, 25, 30, 7, 40, 50, 11]
lista2 = []

# Recorremos la lista para buscar múltiplos de 5
for i in range(len(lista)):
    if lista[i] % 5 == 0:
        lista2.append(lista[i])

# Mostramos el resultado por pantalla
print("Lista de múltiplos de 5:", lista2)