def enumerar(lista):
    for indice, valor in enumerate(lista):
        yield indice, valor


# prueba el generador
colores = ['rojo', 'verde', 'azul']
for indice, color in enumerar(colores):
    print(f"{indice}: {color}")
