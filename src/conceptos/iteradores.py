# Problema: nombre la variable del blucle igual que otra existente
y = 10
squares = []
for x in range(5):
    # Se supone que esta x está dentro del scope del bucle
    squares.append(x ** 2)

print("Cuadrados :", squares)

# x es accesible aquí ya que fue incializada a 10 pero también fue modificada en el bucle
print("x después del bucle:", x)  # Valdrá 4 y no 10

x = 10
# Usar comprensión de lista para crear la lista de cuadrados
squares = [x ** 2 for x in range(5)]

print("Lista de cuadrados:", squares)  # Imprime la lista de cuadrados

# x sigue siendo accesible aquí y retiene su valor original porque 'i' fue usada en la comprensión
print("x después del bucle for:", x)  # Imprime 10


mi_lista = [1, 2, 3]
mi_iterador = iter(mi_lista)  # Crea un iterador para mi_lista

print(next(mi_iterador))  # Imprime 1
print(next(mi_iterador))  # Imprime 2
# y así sucesivamente...
print('-----------------')
# Generador


def contador(maximo):
    n = 0
    while n < maximo:
        yield n  # Produce un valor y congela la función aquí
        n += 1


# Crear un generador
mi_contador = contador(5)

# Iterar sobre el generador
# for numero in mi_contador:
#    print(numero) # Imprime 0, 1, 2, 3, 4

# Otra forma de iterar sobre un generador
try:
    print(next(mi_contador))  # Imprime 0
    print("hola")
    print(next(mi_contador))  # Imprime 1
    print(next(mi_contador))  # Imprime 2
    print(next(mi_contador))  # Imprime 3
    print(next(mi_contador))  # Imprime 4
    print(next(mi_contador))  # Genera una excepción StopIteration
except StopIteration:
    print('Fin')
