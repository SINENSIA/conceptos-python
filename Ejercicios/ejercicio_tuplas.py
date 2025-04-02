# Crea una tupla e intenta modificar su contenido
import copy
mi_tupla = (1, 2, 3)

print(mi_tupla[0])
try:
    mi_tupla[0] = 1
except TypeError:
    print("Error una tupla no se puede modificar")

# Creamos una tupla mixta. Recuerda que una tupla es inmutable y puede contener otro tipos de datos como lsitas, cadenas, enteros, etc.

tupla_mixta = (1, "dos", [3, 4], {5: "cinco"}, (6, 7), 8.0, True, None, {9})

# Pregunta podríamos modificar el contenido del tercer elemento tupla_mixta[2]?
print(tupla_mixta[2])
tupla_mixta[2][0] = 10
print(tupla_mixta)


# Podemos modificar el contenido de una lista que se encuentra dentro de una tupla, pero no podemos modificar el contenido de la tupla en sí.

# Imprime los elementos de la tupla con un loop for y su tipo
# Ejemplo   1 => <class 'int'>
#           dos => <class 'str'>
# Para concatenar el valor del elemento con su tipo tendremos que hacer casting de ambos con str()
for item in tupla_mixta:
    print(str(item) + " => " + str(type(item)))
    # opción usando un fstring
   # print(f"{item} => {type(item)}\n")
print("\n--- Convierte la tupla_mixta a un list e imprímela --- ")
lista_mixta = list(tupla_mixta)
print(lista_mixta)

print("\n----- Modifica el elemento 1 ('dos') de la lista y vuelve a pasar la lista a tupla -----")

lista_mixta[1] = "cambiado"
tupla_mixta = tuple(lista_mixta)
print(tupla_mixta)

print("\n----- Crea una tupla numérica y realiza las operaciones de suma, maximo y minimo -----\n")
tupla_numeros = (5, 10, 3, 8, 2)

print("Suma:", sum(tupla_numeros))
print("Máximo:", max(tupla_numeros))
print("Mínimo:", min(tupla_numeros))

print("------- Calcula los cuadrados de la tupla con una función de compresión -------")
cuadrados = tuple(num ** 2 for num in tupla_numeros)
print(cuadrados)

print("----- Desempequetado ------")
print(f"Tiene {len(cuadrados)} items")

valor1, valor2, valor3, *resto_de_valores = cuadrados
print(valor1, valor2, valor3, resto_de_valores)

lista_original = [[1, 2, 3], [4, 5, 6]]
shallow_copia = lista_original.copy()
lista_original[0][0] = 'X'
print(shallow_copia)

lista_original = [[1, 2, 3], [4, 5, 6]]

deep_copia = copy.deepcopy(lista_original)
lista_original[0][0] = 'X'
print("Original:", lista_original)
print("Deep Copia:", deep_copia)  # No reflejará los cambios
