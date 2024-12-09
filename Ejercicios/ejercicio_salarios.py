from statistics import mean, median, stdev
import json
import os

# Cargar la lista desde el archivo JSON. Cambia por tu ruta relativa! puedes usar os.getcwd() para saber dónde se está ejecutando tu script!

with open('data/personas.json', 'r') as archivo_json:
    personas = json.load(archivo_json)


def get_salary(persona):
    return persona["salario"]


print("--- Creamos una función para mostrar un listado mas legible de personas")


def list_personas_legible(listado_personas):
    for persona in listado_personas:
        print(
            f"ID: {persona['id']}, Edad: {persona['edad']}, Ciudad: {persona['ciudad']}, Salario: {persona['salario']}")


print("\n--- Usando slicing imprime el listado de las primeras 5 personas con la función list_personas_legible ---")
list_personas_legible(personas[:5])

print("\n--- Obtenemos el salario medio, redondea sin decimales y usa un fstring para mostrarlo ---")
salario_medio = round(mean(get_salary(persona) for persona in personas))
print(f"Salario medio: {salario_medio}")

print("""\n--- Obtenemos la mediana del salario, quita los decimales sin redondeo, 
      quedandote sólo con la parte entera y usamos fstring para mostrarlo ---""")

mediana_salario = int(median(get_salary(persona) for persona in personas))
print(f"Mediana: {mediana_salario}")

print("""\n--- usa zip para combinar ciudades y salarios en un listado de tuplas, 
      imprime la quinta ciudad con su salario, desempaquetando y usando un fstring ---""")
# obtenemos salarios y ciudad
salarios = [persona["salario"] for persona in personas]

ciudades = [persona["ciudad"] for persona in personas]

salarios_ciudades = list(zip(ciudades, salarios))

quinta_ciudad, quinto_salario = salarios_ciudades[4]
print(f"Quinta ciudad: {quinta_ciudad} => Salario: {quinto_salario}")

print("""\nCrear un diccionario con los salarios 
      por ciudad e imprime los salarios de la ciudad de Madrid ---""")
salarios_por_ciudad = {}
for persona in personas:
    ciudad = persona["ciudad"]
    salario = persona["salario"]
    if ciudad not in salarios_por_ciudad:
        salarios_por_ciudad[ciudad] = []
    salarios_por_ciudad[ciudad].append(salario)
print(salarios_por_ciudad["Madrid"])

print("\n--- Con una compresión de diccionario calcula la media de salarios por ciudad ---")
media_salarios_por_ciudad = {ciudad: round(
    mean(salarios)) for ciudad, salarios in salarios_por_ciudad.items()}

print(media_salarios_por_ciudad)

print("\n--- Con un lambda filtra las personas que tienen un salario por encima de la media ---")
salarios_sobre_media = list(
    filter(lambda persona: persona["salario"] > salario_medio, personas))
list_personas_legible(salarios_sobre_media)

print("\n--- Con lambdas filtra las personas que tienen un salario por encima de la media de su ciudad ---")
salarios_sobre_media_ciudad = list(filter(
    lambda persona: persona["salario"] > media_salarios_por_ciudad[persona["ciudad"]], personas))
list_personas_legible(salarios_sobre_media_ciudad)

"""
tres_personas_con_mas_salario_sobre_media_ciudad = sorted(
    salarios_sobre_media_ciudad, key=lambda x: x['salario'], reverse=True)[:3]

print(tres_personas_con_mas_salario_sobre_media_ciudad)
"""

print("\n--- Encontrar la persona más joven con el mayor salario (usando una funcion) ---")

"""
def encontrar_persona(lista_personas):
    persona_seleccionada = None
    for persona in lista_personas:
        if persona_seleccionada is None or \
           (persona['salario'] > persona_seleccionada['salario']) or \
           (persona['salario'] == persona_seleccionada['salario'] and persona['edad'] < persona_seleccionada['edad']):
            persona_seleccionada = persona
    return persona_seleccionada
"""

# Opcion 1
personas_ordenadas = sorted(personas, key=lambda x: x['edad'])
personas_ordenadas = sorted(
    personas_ordenadas, key=lambda x: x['salario'], reverse=True)

# print(personas_ordenadas)

# Para no hacer tantos pasadas pordríamos


def criterio_ordenamiento(persona_ord):
    """Usamos un truco para ordenar por dos criterios edad y salario

    Args:
        persona (_type_): dict

    Returns:
        _type_: tuple
    """
    return (-persona_ord['salario'], persona_ord['edad'])


# Ordenamos las personas usando la función 'criterio_ordenamiento'
personas_ordenadas = sorted(personas, key=criterio_ordenamiento)


# La primera persona de la lista ordenada es la más joven con el mayor salario
persona_joven_alto_salario = personas_ordenadas[0]

# Mostrar los datos de la persona seleccionada
print(f"La persona más joven con el mayor salario es: ID: {persona_joven_alto_salario['id']}, "
      f"Edad: {persona_joven_alto_salario['edad']}, Ciudad: {persona_joven_alto_salario['ciudad']}, "
      f"Salario: {persona_joven_alto_salario['salario']}")

print("\n--- Top 5 Listado de personas más jóvenes con salario más alto: ---")
# Paso 1: Ordenar por edad en orden ascendente
personas_ordenadas_por_edad = sorted(personas, key=lambda x: x['edad'])

# Paso 2: Ordenar por salario en orden descendente, sobre la lista ya ordenada por edad
personas_ordenadas_por_salario_y_edad = sorted(
    personas_ordenadas_por_edad, key=lambda x: x['salario'], reverse=True)

# Imprimir el resultado
print(list_personas_legible(personas_ordenadas_por_salario_y_edad[:5]))
