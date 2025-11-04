# Preparar el texto de 1000 líneas como lista de strings
texto_largo = [f"Línea {i + 1}" for i in range(1000)]

bloques = []
bloque_actual = ""
contador_lineas = 0
contador_bloques = 0

for linea in texto_largo:
    bloque_actual += linea + "\n"
    contador_lineas += 1

    if contador_lineas % 25 == 0:
        contador_bloques += 1
        # Almacenar bloque completo sin último salto extra
        bloques.append(bloque_actual.strip())
        print(
            f"\nBloque de texto {contador_bloques}:\n{bloque_actual.strip()}")
        bloque_actual = ""
        # Finalizar después del bloque 3
    
print(f"Total bloques: {contador_bloques}")
# Si quedaron líneas sin cerrar el último bloque
if bloque_actual:
    contador_bloques += 1
    bloques.append(bloque_actual.strip())
    print(
        f"\nBloque de texto final {contador_bloques}:\n{bloque_actual.strip()}")
