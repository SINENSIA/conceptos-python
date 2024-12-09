# Observa el siguiente código
lista = [1, 2, 4, 3, 6]
for elemento in lista:
    if elemento % 2 == 0:
        lista.remove(elemento)
print(lista)

# En la primera iteración el valor uno tiene el índice 0, comoe s impar no se quita.
# En la segunda iteración el valor 2 tiene el índice 1, como es par, se elimina de la lista.
# Aquí es donde ocurre: Al quitar el índice 1 (el valor 2), la lista se reindexa, y el valor 4 que antes era el índice 2, pasa a ser el índice 1.
# Por tanto en la siguiente iteración, se saltará, y se eveluará el índice 2 que ahora es el valor 3.

# ---------------------------------------- Soluciones ------------------------------------------------- #

##################################### Iterear sobre una copia ###########################################
# Lista original
numeros = [1, 2, 3, 4, 5]

# Iteramos sobre una copia de la lista para eliminar elementos (numeros[:] es una copia dinámica de numeros)
for numero in numeros[:]:
    if numero % 2 == 0:
        numeros.remove(numero)

print("Con [:] ", numeros)  # Salida: [1, 3, 5]

# o bien con copy()
numeros = [1, 2, 3, 4, 5]
for numero in numeros.copy():
    if numero % 2 == 0:
        numeros.remove(numero)

print("Con copy: ", numeros)  # Salida: [1, 3, 5]


###################################### Crear una lista de cambios ##########################
# Lista original
numeros = [1, 2, 3, 4, 5]
# Lista para almacenar elementos a eliminar
elementos_para_eliminar = []

# Registrar elementos a eliminar
for numero in numeros:
    if numero % 2 == 0:
        elementos_para_eliminar.append(numero)

# Eliminar elementos registrados (numeros es una lsita y elementos_para_eliminar otra)
for elemento in elementos_para_eliminar:
    numeros.remove(elemento)

print("Con lista de cambios ", numeros)  # Salida: [1, 3, 5]


########################## Usar compresiones #################################
# Lista original
numeros = [1, 2, 3, 4, 5]

# Usar comprensión de lista para filtrar
numeros = [numero for numero in numeros if numero % 2 != 0]

print("Con compresion: ", numeros)  # Salida: [1, 3, 5]
