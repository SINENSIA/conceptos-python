# Preparar el texto de 1000 líneas como una lista de strings, cada una representando una línea
texto_largo = ["\nLínea " + str(i + 1) for i in range(1, 1000)]

# Inicializar variables para almacenar el bloque actual y contar las líneas
# Comenzamos con la primera línea para evitar el salto de línea al inicio
bloque_actual = "\nLinea 1"
contador_lineas = 1
contador_bloques = 0
for linea in texto_largo:
    contador_lineas += 1
    bloque_actual += linea
    # Verificar si se han acumulado 25 líneas en el bloque actual
    if (contador_lineas % 25) == 0:
        contador_bloques += 1
        # Imprimir el bloque de 25 líneas
        print(f"\nBloque de texto {contador_bloques}:\n", bloque_actual)
        bloque_actual = ""  # Reiniciar el bloque para las siguientes 25 líneas
        continue

    # Para evitar agregar un salto de línea adicional al inicio del nuevo bloque
    if bloque_actual == "":
        bloque_actual = linea.strip()

    if (contador_lineas == 51):
        break
# Imprimir cualquier línea restante que no complete un bloque de 25
if bloque_actual:
    print("Bloque de texto final:\n", bloque_actual)
