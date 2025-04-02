

# ------------------------------------------#
# con range
# Preparar el texto de 1000 líneas como una lista de strings
texto_largo = [f"Línea {i}" for i in range(1, 1001)]

bloques = []
contador_bloques = 0

# Iterar en pasos de 25
for i in range(0, len(texto_largo), 25):
    bloque_actual = "\n".join(texto_largo[i:i+25])
    bloques.append(bloque_actual)
    contador_bloques += 1

    print(f"\nBloque de texto {contador_bloques}:\n{bloque_actual}")

    # Finalizar después del bloque que contiene hasta la línea 50
    if i + 25 >= 51:
        break
