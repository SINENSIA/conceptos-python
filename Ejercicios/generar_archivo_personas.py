import random
import json
import os

NUM_PERSONAS = 100
CIUDADES = ["Madrid", "Sevilla", "Barcelona",
            "Valencia", "Bilbao", "Zaragoza", "Málaga", "Murcia"]
EDADES = range(20, 60)
SALARIOS = range(20000, 150001, 5000)
OUTPUT_FILE = 'data/personas.json'


def generar_personas(num_personas):
    return [
        {
            "id": i,
            "edad": random.choice(EDADES),
            "ciudad": random.choice(CIUDADES),
            "salario": random.choice(SALARIOS),
        }
        for i in range(1, num_personas + 1)
    ]


def guardar_json(datos, archivo):
    with open(archivo, 'w') as file:
        json.dump(datos, file, indent=4)


personas = [
    {"id": i, "edad": random.choice(EDADES), "ciudad": random.choice(
        CIUDADES), "salario": random.choice(SALARIOS)}
    for i in range(1, 100)
]
os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

try:
    personas = generar_personas(NUM_PERSONAS)
    guardar_json(personas, OUTPUT_FILE)
    print(f"Archivo guardado correctamente en {OUTPUT_FILE}")
except Exception as e:
    print(f"Error al guardar el archivo: {e}")
