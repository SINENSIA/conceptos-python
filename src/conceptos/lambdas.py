modulo3 = lambda x : x %3

print(modulo3(8))

a = [1, 2, 3, 4, 5, 6]
agrupar_adyacentes = lambda a, k: zip(*([iter(a)] * k))
print(list(agrupar_adyacentes(a, 3)))

# Ejemplo: ordenar lista de tuplas
productos = [('Manzanas', 23), ('Peras', 42), ('Cerezas', 10), ('Fresas', 17)]
productos.sort(key=lambda x: x[1])  # Ordena por el segundo elemento de cada tupla, que es la cantidad
print(productos)  

# Ejemplo en orden descendiente
productos = [('Manzanas', 23), ('Peras', 42), ('Cerezas', 10), ('Fresas', 17)]
productos.sort(key=lambda x: x[1], reverse=True)  # Ordena por el segundo elemento de cada tupla, que es la cantidad
print(productos)  


# Ejemplo: ordenar lista de diccionarios
productos = [{'nombre': 'Manzana', 'precio': 2}, {'nombre': 'Peras', 'precio': 1}, {'nombre': 'Cerezas', 'precio': 10}]
productos.sort(key=lambda x: x['precio'])  # Ordena por el valor de la clave 'precio' de cada diccionario
print(productos)  # [{'nombre': 'Peras', 'precio': 1}, {'nombre': 'Manzana', 'precio': 2}, {'nombre': 'Cereza', 'precio': 10}]

# Ejemplo: ordenar lista de objetos
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f'Producto({self.nombre}, {self.precio})'

productos = [Producto('Manzana', 2), Producto('Peras', 1), Producto('Cerezas', 10)]
productos.sort(key=lambda x: x.precio)  # Ordena por el valor del atributo 'precio' de cada objeto
print(productos)  # [Producto(Banana, 1), Producto(Manzana, 2), Producto(Cereza, 10)]

# Caso de uso: Filtrar elementos de una lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4, 6, 8, 10]

# Caso de uso: Realizar operaciones con cada elemento de una lista
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)  # [1, 4, 9, 16, 25]
