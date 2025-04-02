print("--------------------")
numero = 0
if numero:
    # Tu predicción: el valor 0 es considerado False cuando se evalúa en un contexto booleano
    print("numero es distinto de cero")

mi_array = []
if mi_array:
    # Tu predicción: Este bloque NO se ejecuta porque 0 se considera False en Python
    print("mi_array tiene elementos")

mi_diccionario = {}
if mi_diccionario:
    # Tu predicción: Este bloque NO se ejecuta porque 0 se considera False en Python
    print("mi_diccionario tiene claves")

texto = "Hola"
if texto:
    print("texto tiene contenido")  # Tu predicción: Este si se ejecuta

valor = None
if valor:
    print("valor no es None")  # Tu predicción: Esto no se ejecuta

print(bool(valor))

