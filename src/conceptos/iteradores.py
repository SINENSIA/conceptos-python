mi_lista = [1, 2, 3]
mi_iterador = iter(mi_lista)  # Crea un iterador para mi_lista

print(next(mi_iterador))  # Imprime 1
print(next(mi_iterador))  # Imprime 2
# y así sucesivamente...

## Generador
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
    print(next(mi_contador)) # Imprime 0
    print(next(mi_contador)) # Imprime 1
    print(next(mi_contador)) # Imprime 2
    print(next(mi_contador)) # Imprime 3
    print(next(mi_contador)) # Imprime 4
    print(next(mi_contador)) # Genera una excepción StopIteration
except:
    print('Fin')