
canciones = ["Bohemian Rhapsody", "Stairway to Heaven", "Hotel California", "Imagine", "Smells Like Teen Spirit"]
duraciones = [5.55, 8.02, 6.30, 3.03, 5.01]  # Duraciones en minutos

diccionario = dict(zip(canciones, duraciones))

print(diccionario)

tres_mas_largas = sorted(diccionario, key=lambda k: diccionario[k], reverse=True)[:3]

print("Las tres canciones más largas son:")

for cancion in tres_mas_largas:
    print(cancion)
                   
dict1 = {1: "Uno", 2: "Dos", 3 : "Tres"}
dict2 = {[1,2]: "Uno", [2,3]: "Dos", [3,4]: "Tres"}
dict3 = {"Uno": 1, "Dos": 2, "Tres": 3}
dict4 = {(1,2): "Uno", (2,3): "Dos", (4,5): "Tres"}