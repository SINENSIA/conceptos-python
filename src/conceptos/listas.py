
notas = [5, 6, 7, 8, 9]

elemento = notas.pop()

print(elemento)

lista_numeros = range(0,9)
print(lista_numeros)

productos = ["Televisor", "Afeitadora", "Calentador de agua", "Equipo de sonido", "Cafetera"]
lista = productos[0:3]
print(lista)

# pylint: disable-all
productos = ["Televisor", "Afeitadora", "Calentador de agua", "Equipo de sonido", "Cafetera"]
lista = productos[-2:]
print(lista)

provincias = ["Madrid", "Segovia", "Lugo", "Almería"]

print(provincias[-2:])

alumno = ('Carlos', 'Fundamentos Python', 8.9)

# Listas por comprensión
items = [ 0, 0, 2, 7, 4 , 5, 2 ]
nueva_lista = []
for item in items:
  if (item > 0):
     nueva_lista.append(item * 2)

nueva_lista = [ item * 2 for item in items if item > 0]
print(nueva_lista)

monedas = ['Euro', 'Libra', 'Dólar Mejicano', 'Yen']

precios_dolar = [
    1.2,
    1.38,
    0.05,
    0.009
]

zipped_currencies = zip(monedas, precios_dolar)

print(list(zipped_currencies))

nombres = ["Carlos", "Laura", "Beatriz"]
edades = [45, 23, 37]
diccionario = dict(zip(nombres, edades))
print(diccionario)  # 'Carlos': 45, 'Laura': 23, 'Beatriz': 37}

pares = [(1, 'a'), (2, 'b'), (3, 'c')]
numeros, letras = zip(*pares)
print(numeros)  # (1, 2, 3)
print(letras)  # ('a', 'b', 'c')



for nombre, edad in zip(nombres, edades):
    print(f"{nombre} tiene {edad} años")

