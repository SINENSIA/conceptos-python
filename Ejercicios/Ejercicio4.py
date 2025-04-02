import random


canciones = ["Bohemian Rhapsody", "Stairway to Heaven",
             "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones = [5.55, 8.02, 6.30, 3.03, 5.01]  # Duraciones en minutos

diccionario = dict(zip(canciones, duraciones))

print(diccionario)


def get_duracion(k):
    return diccionario[k]


# tres_mas_largas = sorted(
#    diccionario, key=lambda k: diccionario[k], reverse=True)[:3]
tres_mas_largas = sorted(diccionario, key=get_duracion, reverse=True)[:3]
# tres_mas_largas = sorted(
#    diccionario, key=lambda k: diccionario.get(k), reverse=True)[:3]

print("Las tres canciones más largas son:")

for cancion in tres_mas_largas:
    print(cancion)

seleccionadas = random.sample(list(diccionario.items()), 3)
print()
print("Las tres canciones aleatorias son:")
# canciones random
for titulo, duracion in seleccionadas:
    print(f"Canción: {titulo}, Duración: {duracion:.2f} minutos")
