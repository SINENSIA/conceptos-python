import random
import json

# Generar una lista de personas con valores ficticios
ciudades = ["Madrid", "Sevilla", "Barcelona", "Valencia", "Bilbao", "Zaragoza", "Málaga", "Murcia"]
edades = range(20, 60)
salarios = range(20000, 150001, 5000)

personas = [
    {"id": i, "edad": random.choice(edades), "ciudad": random.choice(ciudades), "salario": random.choice(salarios)}
    for i in range(1, 100)
]
with open('data/personas.json', 'w') as file:
    json.dump(personas, file, indent=4)