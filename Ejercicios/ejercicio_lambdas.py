import math
from statistics import stdev

# Función lambda para obtener el salario

def obtener_salario(persona): return persona["salario"]

# Función para obtener la diferencia entre el salario y el salario medio

def obtener_diferencia_salario(
    persona): return round((persona["salario"] - salario_medio), 2)


# Lista de personas
personas = [
    {"nombre": "Ana", "edad": 25, "ciudad": "Madrid", "salario": 25000},
    {"nombre": "Juan", "edad": 30, "ciudad": "Sevilla", "salario": 30000},
    {"nombre": "María", "edad": 22, "ciudad": "Madrid", "salario": 22000},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona", "salario": 35000},
]

# Calcular el salario medio
salario_total = sum(map(obtener_salario, personas))
salario_medio = math.floor(salario_total / len(personas))

# Calcular la desviación estándar del salario
diferencias_salario = list(map(obtener_diferencia_salario, personas))
# O bien con compresion diferencias_salario = [obtener_diferencia_salario(persona, salario_medio) for persona in personas]
desviacion_estandar = round(stdev(diferencias_salario), 2)

# Obtener la persona con el mayor ratio salario/edad

def ratio_salario_edad(persona): return persona["salario"] / persona["edad"]


persona_mayor_ratio = max(personas, key=lambda persona: (
    ratio_salario_edad(persona), persona["salario"]))

# Imprimir resultados
print("Salario medio:", salario_medio)
print("Desviación estándar del salario:", desviacion_estandar)
print("Persona con el mayor ratio salario/edad:", persona_mayor_ratio)
