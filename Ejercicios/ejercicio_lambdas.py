from statistics import stdev

# Función lambda para obtener el salario
obtener_salario = lambda persona: persona["salario"]

# Función lambda para obtener la diferencia entre el salario y el salario medio
obtener_diferencia_salario = lambda persona: persona["salario"] - salario_medio

# Lista de personas
personas = [
    {"id": 1, "nombre": "Ana", "edad": 25, "ciudad": "Madrid", "salario": 25000},
    {"nombre": "Juan", "edad": 30, "ciudad": "Sevilla", "salario": 30000},
    {"nombre": "María", "edad": 22, "ciudad": "Madrid", "salario": 22000},
    {"nombre": "Pedro", "edad": 35, "ciudad": "Barcelona", "salario": 35000},
]

# Calcular el salario medio
salario_total = sum(map(obtener_salario, personas))
salario_medio = salario_total / len(personas)

# Calcular la desviación estándar del salario
diferencias_salario = list(map(obtener_diferencia_salario, personas))
desviacion_estandar = stdev(diferencias_salario)

# Obtener la persona con el mayor ratio salario/edad
ratio_salario_edad = lambda persona: persona["salario"] / persona["edad"]
persona_mayor_ratio = max(personas, key=ratio_salario_edad)

# Imprimir resultados
print("Salario medio:", salario_medio)
print("Desviación estándar del salario:", desviacion_estandar)
print("Persona con el mayor ratio salario/edad:", persona_mayor_ratio)
