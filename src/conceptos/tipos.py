# Tipos en Python
# Enteros
edad = 20

# Flotantes
peso = 60.5

# Booleanos
es_estudiante = True
es_profesor = False

# Cadenas de texto
nombre = "Juan"
apellido = "Perez"
mi_cadena = "Hola Mundo"
mi_cadena[1] # → o
mi_cadena[1:4] # → ola
mi_cadena + "!" # → Hola Mundo!
mi_cadena * 2 # → Hola MundoHola Mundo
len(mi_cadena) # → 10
mi_cadena.lower() # → hola mundo
mi_cadena.upper() # → HOLA MUNDO
" Hola Mundo ".strip() # → Hola Mundo
"Hola,Mundo".split(",") # → ['Hola', 'Mundo']
", ".join(['Hola', 'Mundo']) # → Hola, Mundo
mi_cadena.replace("Mundo", "Python") # → Hola Python
mi_cadena.find("Mundo") # → 5
"{} {}".format("Hola", "Mundo") # → Hola Mundo
    # Complejos
complejo = 2 + 3j

# Listas
numeros = [1, 2, 3, 4, 5]
nombres = ["Juan", "Maria", "Luis"]
mezcla = [1, "Juan", True, 3.5]
mi_lista = [1 ,2, 3]
mi_lista.append(4) # → [1, 2, 3, 4]
mi_lista.remove(2) # → [1, 3]
mi_lista.pop() # → 3 (y la lista queda [1, 2])

mi_lista.reverse() # → [3, 2, 1]
mi_lista.sort() # → [1, 2, 3]
mi_lista.insert(1, 'a') # → [1, 'a', 2, 3]
mi_lista.clear() # → []
# la volvemos a construir
mi_lista = [1 ,2, 3]
mi_lista.extend([4, 5]) # → [1, 2, 3, 4, 5]
mi_lista.index(3) # → 2
mi_lista.count(1) # → 1
tareas = ["Lleva a los niños al cole", "Lavar el coche", "Programar una app en python"]
tareas.append("Ir al gimnasio")  # Añadir una nueva tarea
tareas.pop(3)  # Eliminar "Ir al gimnasio" ya que me da pereza volver
tareas.sort()  # Ordenar las tareas

# Tuplas
coordenadas = (10, 20)
mi_tupla = (1, 2, 3)
mi_tupla[0] # → 1
mi_tupla[1:3] # → (2, 3)
mi_tupla + (4, 5) # → (1, 2, 3, 4, 5)
mi_tupla * 2 # → (1, 2, 3, 1, 2, 3)
mi_tupla.index(2) # → 1
mi_tupla.count(2) # → 1
len(mi_tupla) # → 3
a, b, c = mi_tupla # → a = 1, b = 2, c = 3
[x for x in mi_tupla] # → [1, 2, 3]
coordenadas = (40.7128, -74.0060)  # Coordenadas de Nueva York
latitud = coordenadas[0]  # 40.7128
longitud = coordenadas[1]  # -74.0060
latitud, longitud = coordenadas  # latitud = 40.7128, longitud = -74.0060
[x for x in coordenadas] # → [40.7128, -74.0060]

# Conjuntos (Set)
mi_conjunto = {1, 2, 3}
mi_conjunto.add(4) # → {1, 2, 3, 4}
mi_conjunto.remove(3) # → {1, 2, 4}
mi_conjunto.discard(2) # → {1, 4}
mi_conjunto.pop() # → Retorna un elemento aleatorio.
mi_conjunto.clear() # → {}
mi_conjunto | {4, 5} # → {1, 2, 3, 4, 5}
mi_conjunto & {2, 3, 4} # → {2, 3}
mi_conjunto - {2, 3} # → {1}
mi_conjunto ^ {2, 3, 4} # → {1, 4}
len(mi_conjunto) # → 3
[x for x in mi_conjunto] # → [1, 2, 3]

alumnos_python = {"Carlos", "Diego", "Gabriel"}
alumnos_java = {"Diego", "Sofía", "Luís"}

alumnos_comunes = alumnos_python & alumnos_java  # {"Diego"}
# Diccionarios
persona = {
    "nombre": "Juan",
    "apellido": "Perez",
    "edad": 20
}
mi_diccionario = {'uno': 1, 'dos': 2, 'tres': 3}
mi_diccionario['dos'] # → 2
mi_diccionario['dos'] = 22 # → {'uno': 1, 'dos': 22, 'tres': 3}
mi_diccionario.keys() # → dict_keys(['uno', 'dos', 'tres'])
mi_diccionario.values() # → dict_values([1, 22, 3])
mi_diccionario.items() # → dict_items([('uno', 1), ('dos', 22), ('tres', 3)])
mi_diccionario.get('cuatro') # → None
mi_diccionario.setdefault('cuatro', 4) # → 4
mi_diccionario.pop('tres') # → 3
mi_diccionario.popitem() # → ('tres', 3)
mi_diccionario.update({'cinco': 5}) # → {'uno': 1, 'dos': 22, 'cinco': 5}
mi_diccionario.clear() # → {}
# Sets
numeros = {1, 2, 3, 4, 5}
nombres = {"Juan", "Maria", "Luis"}
mezcla = {1, "Juan", True, 3.5}

contactos = {
    "Yolanda": "yoli@example.com",
    "Carlos": "charly@example.com",
    "Pedro": "pedro@contacto.es"
}

email_yolanda = contactos["Yolanda"]  # Acceder al email de Yolanda
contactos["Carlos"] = "madrid@sinensia.com"  # Añadir un nuevo contacto

# None
nada = None

# Imprimir el tipo de dato de una variable
print(type(edad))  # <class 'int'>
print(type(peso))  # <class 'float'>
print(type(es_estudiante))  # <class 'bool'>
print(type(nombre))  # <class 'str'>
print(type(numeros))  # <class 'list'>
print(type(coordenadas))  # <class 'tuple'>
print(type(persona))  # <class 'dict'>
print(type(nada))  # <class 'NoneType'>

    
## Conversiones explícitas
numero = int("123") # Salida: 123
numero = float("123")  # Salida: 1.23
numero = str(123)  # Salida: "123"
lista = list(str(123))  # Salida: [1, 2, 3]
tupla = tuple(str(123))  # Salida: (1, 2, 3)
diccionario = dict([(index,x) for index,x in enumerate("123")])  # Salida: {0: 1, 1: 2, 2: 3}
bool("123")  # Salida: True

## Perdida de precisión
entero = 1000000000
double = 0.0000000001

# Realizamos una operación simple
resultado = entero + double

# Imprimimos el resultado
print("Resultado esperado: 1000000000.0000000001")
print(f"Resultado obtenido: {resultado}")

from decimal import Decimal, getcontext

# Establece la precisión deseada
getcontext().prec = 20

entero = Decimal('1000000000')
double = Decimal('0.0000000001')

resultado = entero + double
print("Resultado con precisión ajustada:", resultado)
