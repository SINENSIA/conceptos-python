# ------------------------------------------#
import os

ruta = os.path.dirname(os.path.abspath(__file__))
ruta_archivo = os.path.join(ruta, "rockyou.txt")
# Con enumerate
# texto de 1000 líneas como una lista de strings, cada una representando una línea
texto_largo = [f"Línea {i}" for i in range(1, 1001)]
bloque_actual = []
bloques = []

for i, linea in enumerate(texto_largo, start=1):
    bloque_actual.append(linea)

    # Cuando se acumulan 25 líneas, se guarda el bloque y se reinicia
    if i % 25 == 0:
        bloques.append(bloque_actual)
        bloque_actual = []

# Verificar cantidad de bloques creados
print(f"Total de bloques creados: {len(bloques)}")

# Mostrar las líneas del primer bloque
for linea in bloques[0:2]:
    print('===============================')
    print(linea)
